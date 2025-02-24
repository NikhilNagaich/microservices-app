# Use Python as base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY app.py .
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 8081
EXPOSE 8081

# Run Flask app
CMD ["python", "app.py"]
