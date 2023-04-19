FROM python:3.10.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH="/opt/app:${PYTHONPATH}"
ENV DJANGO_SETTINGS_MODULE=app.settings.prod
ENV WSGI_LOG_LEVEL=warning
ENV APP_LOG_LEVEL=WARNING
ENV DATABASE_DSN=postgres://postgres:postgres@default:5432/db
ENV RABBITMQ_DSN=amqp://guest:guest@rabbitmq//

WORKDIR /opt/app
ADD app_/ .

RUN pip install -r requirements.txt --quiet --no-cache-dir

CMD [ "gunicorn", \
    "--bind", "0.0.0.0:80", \
    "--user", "www-data", \
    "--group", "www-data", \
    "--log-level", "$WSGI_LOG_LEVEL", \
    "wsgi:app" \
]
