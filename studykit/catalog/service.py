from __future__ import annotations

import re
import uuid
from datetime import UTC, datetime, timedelta

from sqlalchemy import select, text, update
from sqlalchemy.orm import Session

from studykit.domain.models import Job, JobStatus, Kit, KitStatus

_SLUG_RE = re.compile(r"[^a-z0-9-]+")


def slugify(value: str) -> str:
    slug = value.lower().strip()
    slug = re.sub(r"\s+", "-", slug)
    slug = _SLUG_RE.sub("", slug).strip("-")
    return slug[:70] or "kit"


class CatalogService:
    def __init__(self, session: Session):
        self.session = session

    def create_kit(self, *, filename: str, source_path: str, title: str) -> tuple[Kit, Job]:
        kit = Kit(
            id=str(uuid.uuid4()),
            title=title,
            original_filename=filename,
            source_path=source_path,
            status=KitStatus.uploaded.value,
        )
        job = Job(id=str(uuid.uuid4()), kit_id=kit.id, status=JobStatus.queued.value)
        self.session.add(kit)
        self.session.flush()
        job.kit_id = kit.id
        self.session.add(job)
        self.session.commit()
        self.session.refresh(kit)
        self.session.refresh(job)
        return kit, job

    def get_kit(self, kit_id: str) -> Kit | None:
        return self.session.get(Kit, kit_id)

    def get_by_slug(self, slug: str) -> Kit | None:
        return self.session.scalar(select(Kit).where(Kit.slug == slug))

    def list_kits(self, limit: int = 50) -> list[Kit]:
        stmt = select(Kit).order_by(Kit.created_at.desc()).limit(limit)
        return list(self.session.scalars(stmt))

    def latest_job(self, kit_id: str) -> Job | None:
        stmt = select(Job).where(Job.kit_id == kit_id).order_by(Job.created_at.desc())
        return self.session.scalars(stmt).first()

    def set_status(self, kit: Kit, status: KitStatus, error: str | None = None) -> None:
        kit.status = status.value
        kit.error = error
        kit.updated_at = datetime.now(UTC)
        self.session.add(kit)
        self.session.commit()

    def enqueue_retry(self, kit: Kit) -> Job:
        kit.status = KitStatus.uploaded.value
        kit.error = None
        job = Job(id=str(uuid.uuid4()), kit_id=kit.id, status=JobStatus.queued.value)
        self.session.add_all([kit, job])
        self.session.commit()
        self.session.refresh(job)
        return job

    def publish(self, kit: Kit, desired_slug: str | None = None) -> Kit:
        if kit.status != KitStatus.review.value:
            raise ValueError("only kits in review can be published")
        if not kit.artifact_path:
            raise ValueError("kit has no rendered artifact")
        base = slugify(desired_slug or kit.title)
        slug = base
        n = 2
        while self.get_by_slug(slug) and (not kit.slug or kit.slug != slug):
            slug = f"{base}-{n}"
            n += 1
        kit.slug = slug
        kit.status = KitStatus.published.value
        self.session.add(kit)
        self.session.commit()
        self.session.refresh(kit)
        return kit

    def claim_job(self, worker_id: str, lease_seconds: int) -> Job | None:
        now = datetime.now(UTC)
        until = now + timedelta(seconds=lease_seconds)
        dialect = self.session.bind.dialect.name if self.session.bind is not None else "sqlite"
        if dialect == "postgresql":
            row = self.session.execute(
                text(
                    """
                    SELECT id FROM jobs
                    WHERE status = :queued
                       OR (status = :running AND (locked_until IS NULL OR locked_until < :now))
                    ORDER BY created_at
                    FOR UPDATE SKIP LOCKED
                    LIMIT 1
                    """
                ),
                {"queued": JobStatus.queued.value, "running": JobStatus.running.value, "now": now},
            ).first()
            if not row:
                return None
            self.session.execute(
                update(Job)
                .where(Job.id == row.id)
                .values(
                    status=JobStatus.running.value,
                    locked_by=worker_id,
                    locked_until=until,
                    started_at=now,
                )
            )
            self.session.commit()
            return self.session.get(Job, row.id)

        job = self.session.scalars(
            select(Job)
            .where(
                (Job.status == JobStatus.queued.value)
                | (
                    (Job.status == JobStatus.running.value)
                    & ((Job.locked_until.is_(None)) | (Job.locked_until < now))
                )
            )
            .order_by(Job.created_at)
        ).first()
        if not job:
            return None
        job.status = JobStatus.running.value
        job.locked_by = worker_id
        job.locked_until = until
        job.started_at = now
        self.session.add(job)
        self.session.commit()
        self.session.refresh(job)
        return job

    def finish_job(self, job: Job, ok: bool, error: str | None = None) -> None:
        job.status = JobStatus.done.value if ok else JobStatus.failed.value
        job.error = error
        job.finished_at = datetime.now(UTC)
        job.locked_until = None
        self.session.add(job)
        self.session.commit()
