from fastapi import FastAPI
from app.routes import health,items

app = FastAPI(title="FastAPI Fundamentals")

app.include_router(health.router)

app.include_router(items.router)
