import redis, ast

REDIS_HOST = "redis"
QueueName = "job_queue"

r = redis.Redis(host=REDIS_HOST,port=6379,decode_responses=True)

def fetch_job():
    job = r.brpop(QueueName)
    if(job):
        key, value = job
        return ast.literal_eval(value)