from fastapi import FastAPI
from app.routes import health, job_routes

app = FastAPI(title="FastAPI Platform")

app.include_router(health.router, prefix="/api")
app.include_router(job_routes.router, prefix="/api")