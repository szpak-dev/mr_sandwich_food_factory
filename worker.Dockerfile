FROM python:3.10.8-slim

ENV APP_LOG_LEVEL='WARNING'
ENV DATABASE_DSN='postgres://postgres:postgres@default:5432/db'
ENV RABBITMQ_DSN='amqp://guest:guest@rabbitmq//'

WORKDIR /opt/app
ADD app_/ .

RUN pip install -r requirements.txt && \
    apt-get -qq clean && \
    apt-get -qq autoclean && \
    apt-get -qq remove --purge --auto-remove --yes && \
    rm -rf /var/lib/apt/lists/*
