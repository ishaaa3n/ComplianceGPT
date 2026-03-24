FROM python:3.12-slim

WORKDIR /app

# Install dependencies first (cached layer — only re-runs if requirements.txt changes)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code is mounted as a volume in docker-compose, so no COPY . . needed here
# This keeps the image lean and hot-reload working

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
