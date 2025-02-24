from celery import Celery
import time

celery_app = Celery(
    'worker',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)

@celery_app.task(name="worker.process_task")
def process_task():
    print("Processing task...")
    time.sleep(5)
    print("Task completed!")
