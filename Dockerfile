FROM python:3.11-slim

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT ["python", "/app/main.py"]