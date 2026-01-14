from fastapi import FastAPI
from app.routes import health, job_routes
import os

required_envs=["DATABASE_URL","REDIS_HOST"]

for env in required_envs:
    if not os.getenv(env):
        raise RuntimeError(f"Missing required env var: {env}")

app = FastAPI(title="FastAPI Platform")

app.include_router(health.router, prefix="/api")
app.include_router(job_routes.router, prefix="/api")