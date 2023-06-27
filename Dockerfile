FROM python:3.9.0
MAINTAINER Victor Developer Back-end

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
