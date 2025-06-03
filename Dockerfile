# Uses official Python base image
FROM python:3.10-slim

# Sets up a working directory in the container
WORKDIR /app

# Copying requirements  
COPY requirements.txt .

# Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying the app code
COPY main.py .

# Exposes the port for FastAPI 
EXPOSE 8000

# Starts the server using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]