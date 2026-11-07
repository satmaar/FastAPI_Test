# Basic FastAPI App

A beginner-friendly API built for the CAIE Course assignment. It has a JSON welcome route, a
personalized greeting route, and FastAPI's generated interactive documentation.

## Set up

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

Open <http://127.0.0.1:8000/> for the welcome response, try
<http://127.0.0.1:8000/greet/Ada>, and visit <http://127.0.0.1:8000/docs> for the interactive
API documentation.

## Verify

```bash
python -m pip install httpx pytest
pytest -q
```

The verification suite checks both JSON endpoints and the generated API docs. Browser evidence is
saved in `evidence/` after running the app locally.
