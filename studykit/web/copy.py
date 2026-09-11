"""Spanish copy for the authoring pipeline (not the student kit)."""

STATUS = {
    "uploaded": {
        "label": "En cola",
        "title": "Archivo recibido",
        "detail": "El worker tomará el archivo en unos segundos y armará el kit.",
        "step": 2,
        "tone": "wait",
    },
    "compiling": {
        "label": "Generando",
        "title": "Extrayendo temas y preguntas",
        "detail": "Esto suele tardar menos de un minuto. No cierres esta pestaña.",
        "step": 2,
        "tone": "wait",
    },
    "rendering": {
        "label": "Armando el HTML",
        "title": "Escribiendo el kit",
        "detail": "Último paso automático: práctica, fórmulas y hoja exprés.",
        "step": 2,
        "tone": "wait",
    },
    "review": {
        "label": "Para revisar",
        "title": "El kit ya se puede abrir",
        "detail": "Mira el preview. Si las preguntas están bien, publícalo con un enlace corto.",
        "step": 3,
        "tone": "ok",
    },
    "published": {
        "label": "Publicado",
        "title": "Los alumnos ya pueden entrar",
        "detail": "Copia el enlace público. Puedes volver a esta página cuando quieras.",
        "step": 4,
        "tone": "ok",
    },
    "failed": {
        "label": "Falló",
        "title": "No se pudo generar",
        "detail": "Revisa el mensaje, corrige el archivo o reintenta. El original se conservó.",
        "step": 2,
        "tone": "bad",
    },
}

STEPS = (
    {"n": 1, "key": "upload", "label": "Subir"},
    {"n": 2, "key": "generate", "label": "Generar"},
    {"n": 3, "key": "review", "label": "Revisar"},
    {"n": 4, "key": "publish", "label": "Publicar"},
)

BUSY = frozenset({"uploaded", "compiling", "rendering"})


def status_view(code: str) -> dict:
    return STATUS.get(code, STATUS["uploaded"])
