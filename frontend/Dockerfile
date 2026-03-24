FROM python:3.12-slim

WORKDIR /app

# Install dependencies first (cached layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code is mounted as a volume in docker-compose
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
