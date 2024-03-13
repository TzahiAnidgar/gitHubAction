# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .
# Install Python dependencies

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip
# Copy the rest of your application's code into the container
COPY .. .

# Command to run when starting the container
CMD ["python", "api_test.py"]
