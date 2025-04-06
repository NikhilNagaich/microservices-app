import os
import redis
import time
import json

redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
r = redis.from_url(redis_url)

def handle_task(task_data):
    print("Handling task:", task_data)

def run_worker():
    print("Worker started")
    while True:
        task = r.blpop('task_queue', timeout=5)
        if task:
            _, task_data = task
            handle_task(json.loads(task_data))

if __name__ == '__main__':
    run_worker()
