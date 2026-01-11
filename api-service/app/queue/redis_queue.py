# sends job → Redis → Worker will pick
import redis, uuid
from app.config import REDIS_HOST, REDIS_PORT

r=redis.Redis(host = REDIS_HOST, port = REDIS_PORT, decode_responses = True)

QueueName="job_queue"

def push_job(data: dict):
    job_id = str(uuid.uuid4)
    data[job_id] = job_id
    r.lpush(QueueName, str(data))
    return job_id