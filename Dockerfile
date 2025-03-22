FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY server.py .

# Environment variables
ENV PORT=8080

# Expose port
EXPOSE 8080

# Run the server
CMD ["python", "server.py"]
