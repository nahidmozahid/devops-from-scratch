# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements (if you have one, otherwise just install flask)
# We'll create requirements.txt with Flask
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY . .

# Expose port 5008
EXPOSE 5008

# Command to run the app
CMD ["python", "app.py"]
