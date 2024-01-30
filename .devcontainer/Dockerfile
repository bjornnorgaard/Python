FROM python:3.10-slim-buster
WORKDIR /workspace

RUN pip install pytest

COPY requirements.txt .
RUN pip install -r requirements.txt
