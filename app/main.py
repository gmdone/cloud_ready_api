from fastapi import FastAPI
from app.routes import health

app = FastAPI(title="Cloud Ready API")

app.include_router(health.router)