"""A small introductory FastAPI application."""

from fastapi import FastAPI

app = FastAPI(
    title="Basic FastAPI App",
    description="A beginner-friendly API with a welcome route and a greeting route.",
    version="1.0.0",
)


@app.get("/", summary="Welcome", tags=["Welcome"])
async def read_root() -> dict[str, str]:
    """Return a welcome message."""
    return {"message": "Hello, FastAPI"}


@app.get("/greet/{name}", summary="Greet someone", tags=["Greetings"])
async def greet(name: str) -> dict[str, str]:
    """Return a greeting for the supplied name."""
    return {"message": f"Hello, {name}!"}
