# Base image with Python
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python application files to the container
COPY main.py /app

# Install the required dependencies
RUN pip install sentry-sdk

# Run the Python application
CMD ["python", "main.py"]
