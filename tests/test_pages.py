def test_home_lists_example(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Studykit" in response.text
    assert "/k/matematica-iv" in response.text
    assert "Subir" in response.text
    assert "Generar" in response.text


def test_ui_upload_wrong_token_stays_on_form(client):
    response = client.post(
        "/ui/upload",
        data={"token": "nope"},
        files={"file": ("a.md", b"# Hola", "text/markdown")},
    )
    assert response.status_code == 401
    assert "token no coincide" in response.text.lower()
    assert "Sube el temario" in response.text


def test_ui_upload_redirects_with_flash(client):
    response = client.post(
        "/ui/upload",
        data={"token": "test-token"},
        files={"file": ("notas.md", b"# Historia", "text/markdown")},
        follow_redirects=False,
    )
    assert response.status_code == 303
    location = response.headers["location"]
    assert "/kits/" in location
    assert "just=uploaded" in location
    page = client.get(location)
    assert page.status_code == 200
    assert "Archivo en cola" in page.text
    assert "En cola" in page.text
