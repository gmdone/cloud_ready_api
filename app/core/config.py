from fastapi import FastAPI
from app.routes import health

app = FastAPI (title="API para Cloud")

app.include_route(health.router)