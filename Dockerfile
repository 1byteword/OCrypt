FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y gcc python3-dev && \
    pip install -r requirements.txt && \
    apt-get remove -y gcc python3-dev && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 8000

CMD ["python", "app.py"]
