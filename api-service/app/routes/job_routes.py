# Basic job submission API (we’ll power it later)
from fastapi import APIRouter
from app.queue.redis_queue import push_job

router = APIRouter()

@router.post("/job")
def create_job():
    job_id = push_job({
        "task" : "process_file"
    })
    return {
        "message" : "job submitted", 
        "job_id" : job_id
    }