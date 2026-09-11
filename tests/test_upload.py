from studykit.compiler.stub import fixture_schema
from studykit.worker import process_one


def test_upload_requires_token(client):
    response = client.post("/kits", files={"file": ("a.md", b"# Hola", "text/markdown")})
    assert response.status_code == 401


def test_upload_rejects_pdf(client):
    response = client.post(
        "/kits",
        files={"file": ("a.pdf", b"%PDF", "application/pdf")},
        headers={"X-Upload-Token": "test-token"},
    )
    assert response.status_code == 400


def test_upload_process_preview_publish(client):
    schema = fixture_schema()
    response = client.post(
        "/kits",
        files={"file": ("demo.json", schema.model_dump_json().encode(), "application/json")},
        headers={"X-Upload-Token": "test-token"},
    )
    assert response.status_code == 201
    kit_id = response.json()["id"]

    assert process_one() is True

    status = client.get(f"/kits/{kit_id}").json()
    assert status["status"] == "review"
    assert status["job"]["status"] == "done"

    preview = client.get(f"/kits/{kit_id}/preview", headers={"X-Upload-Token": "test-token"})
    assert preview.status_code == 200
    assert 'id="view-inicio"' in preview.text
    assert "function shuffle" in preview.text

    published = client.post(
        f"/kits/{kit_id}/publish",
        headers={"X-Upload-Token": "test-token"},
        data={"slug": "demo-kit"},
    )
    assert published.status_code == 200
    assert published.json()["slug"] == "demo-kit"

    public = client.get("/k/demo-kit")
    assert public.status_code == 200
    assert "KIT_DATA" in public.text


def test_example_fallback_route(client):
    response = client.get("/k/matematica-iv")
    assert response.status_code == 200
    assert "Matemática IV" in response.text


def test_generated_example_route(client):
    response = client.get("/k/matematica-iv/generated")
    assert response.status_code == 200
    assert 'id="view-formulas"' in response.text
    assert 'id="view-expres"' in response.text
