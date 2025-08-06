# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*
# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY . .

# Expose the default port
EXPOSE 8080
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Run FastAPI app
ENV PORT=8080
CMD ["sh", "-c", "python -m uvicorn main:app --host=0.0.0.0 --port=$PORT"]
