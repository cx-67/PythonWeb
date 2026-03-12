# Python Web Demo

This is a lightweight Python web project built with FastAPI.

## Features

- Home page rendered with Jinja2 templates
- Health check API at `/api/health`
- Interactive API docs at `/docs`
- Basic test suite with pytest

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000 in your browser.

## Run tests

```bash
pytest
```