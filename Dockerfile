# Use a lightweight Python base image
FROM python:3.9-slim

# Set environment variables to prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy requirements file first, to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the application with database initialization
CMD ["python", "run.py","--host =0.0.0.0", "--port=8000"]
