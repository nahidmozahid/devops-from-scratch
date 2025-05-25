# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Expose port 5000 (Flask app port)
EXPOSE 5000

# Set environment variable for Flask to listen on all interfaces
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run the app
CMD ["python", "app.py"]
