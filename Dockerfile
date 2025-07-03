FROM python:3.11-slim

RUN apt-get update && apt-get install -y iputils-ping

WORKDIR /app

COPY utility.py .

ENTRYPOINT ["python3", "utility.py"]
