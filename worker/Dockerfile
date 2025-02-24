# Use Python as base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY worker.py .
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Run Celery worker
CMD ["celery", "-A", "worker", "worker", "--loglevel=info"]
