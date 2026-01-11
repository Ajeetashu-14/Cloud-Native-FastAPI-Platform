from worker.queue.redis_listener import fetch_job
from worker.processor.file_processor import process_job

print("worker starting listening.....")

while True:
    job = fetch_job()
    if job():
        process_job(job)