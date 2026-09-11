from typing import Literal

from pydantic import BaseModel, Field, model_validator


class Formula(BaseModel):
    label: str
    eq: str
    note: str = ""


class ExpressLine(BaseModel):
    n: int
    text: str
    hide: str = ""


class Item(BaseModel):
    type: Literal["mc", "num"]
    prompt: str
    hint: str
    explain: str
    cat: str = ""
    opts: list[str] | None = None
    correct: int | None = None
    answer: float | None = None
    tol: float = 0.01

    @model_validator(mode="after")
    def answers_match_type(self) -> "Item":
        if self.type == "mc":
            if not self.opts or len(self.opts) < 2:
                raise ValueError("mc items need at least two opts")
            if self.correct is None or not (0 <= self.correct < len(self.opts)):
                raise ValueError("mc items need a valid correct index")
        if self.type == "num" and self.answer is None:
            raise ValueError("num items need an answer")
        if not self.prompt.strip() or not self.hint.strip() or not self.explain.strip():
            raise ValueError("prompt, hint and explain are required")
        return self


class Block(BaseModel):
    id: str
    name: str
    weight: int = Field(gt=0, le=100)
    topics: list[str]
    formulas: list[Formula] = Field(default_factory=list)
    bank: list[Item]


class KitSchema(BaseModel):
    title: str
    kicker: str
    subtitle: str = ""
    blocks: list[Block]
    express: list[ExpressLine] = Field(default_factory=list)
    session_len: int = 8
    full_len: int = 20
    points_per_item: int = 5

    @model_validator(mode="after")
    def kit_is_playable(self) -> "KitSchema":
        if not self.title.strip():
            raise ValueError("title is required")
        if not self.blocks:
            raise ValueError("at least one block is required")
        ids: set[str] = set()
        for block in self.blocks:
            if block.id in ids:
                raise ValueError(f"duplicate block id: {block.id}")
            ids.add(block.id)
            if not block.bank:
                raise ValueError(f"block {block.id} has no items")
            if not block.topics:
                raise ValueError(f"block {block.id} has no topics")
        total = sum(block.weight for block in self.blocks)
        if total != 100:
            raise ValueError(f"block weights must sum to 100, got {total}")
        return self

    def full_plan(self) -> list[dict]:
        """How many simulacro questions each block contributes (≈ full_len)."""
        raw = []
        for block in self.blocks:
            count = max(1, round(block.weight / self.points_per_item))
            count = min(count, len(block.bank))
            raw.append({"id": block.id, "count": count})
        total = sum(row["count"] for row in raw)
        # Nudge the largest banks so the plan matches full_len when possible.
        target = min(self.full_len, sum(len(b.bank) for b in self.blocks))
        banks = {b.id: len(b.bank) for b in self.blocks}
        guard = 0
        while total < target and guard < 40:
            grew = False
            for row in sorted(raw, key=lambda r: -r["count"]):
                if row["count"] < banks[row["id"]]:
                    row["count"] += 1
                    total += 1
                    grew = True
                    if total >= target:
                        break
            if not grew:
                break
            guard += 1
        while total > target:
            for row in sorted(raw, key=lambda r: -r["count"]):
                if row["count"] > 1:
                    row["count"] -= 1
                    total -= 1
                    break
            else:
                break
        return raw
