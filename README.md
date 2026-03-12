# Python Web Demo

This is a lightweight Python web project built with FastAPI.

## Features

- Home page rendered with Jinja2 templates
- Health check API at `/api/health`
- Interactive API docs at `/docs`
- Basic test suite with pytest

## Run locally

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Ubuntu or Debian

If `apt install` returns `404 Not Found`, refresh package indexes first:

```bash
sudo apt update
```

Then install the required system packages:

```bash
sudo apt install python3.12-venv python3-pip
```

Create and activate the virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

If you do not want to use a virtual environment temporarily, you can still install dependencies for the current user:

```bash
python3 -m pip install --user -r requirements.txt
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Open http://127.0.0.1:8000 in your browser.

## Run tests

```bash
pytest
```