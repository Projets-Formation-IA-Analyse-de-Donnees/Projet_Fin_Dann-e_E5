# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY app.py .

RUN pip install streamlit prometheus_client

EXPOSE 8501 8000

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
