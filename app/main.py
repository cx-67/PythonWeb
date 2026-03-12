from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

app = FastAPI(
    title="Python Web Demo",
    description="A lightweight FastAPI web project.",
    version="1.0.0",
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "Python Web Demo",
            "message": "FastAPI project is running.",
        },
    )


@app.get("/api/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}