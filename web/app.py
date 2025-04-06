from flask import Flask, jsonify, request
import os
import redis
import json

app = Flask(__name__)
redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
r = redis.from_url(redis_url)

@app.route('/')
def home():
    return jsonify({'message': 'Web Service is Running'}), 200

@app.route('/task', methods=['POST'])
def create_task():
    data = request.get_json()
    r.rpush('task_queue', json.dumps(data))
    return jsonify({'message': 'Task added to queue'}), 202

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
