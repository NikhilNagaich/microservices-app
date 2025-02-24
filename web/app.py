from flask import Flask
import psycopg2
from celery import Celery

celery_app = Celery(
    'tasks',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)

app = Flask(__name__)

# Connect to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    return conn

@app.route('/')
def index():
    name = "Nikhil Nagaich"
    roll_number = "2022BCD0032"
    bio = "I am a student at IIIT Kottayam, pursuing my Bachelors in Computer Science Engineering with specialization in Aritificial Intelligence and Data Science."

    return f"""
    <h1>Hello, {name} ({roll_number})!</h1>
    <p>{bio}</p>
    <p>Visit /task to add a task to the worker queue.</p>
    """

@app.route('/task')
def add_task():
    celery_app.send_task("worker.process_task")  # Send task using Celery
    return "Task added to the worker queue!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
