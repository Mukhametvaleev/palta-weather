FROM python:3.9.5-slim AS compile-image
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY palta_weather/ /usr/src/app

FROM python:3.9.5-slim AS build-image
ENV APP_NAME=$APP_NAME COORD=$COORD SCHEDULE=$SCHEDULE PATH="/opt/venv/bin:$PATH"
COPY --from=compile-image /opt/venv /opt/venv
COPY ./compose/local/flask/check_db_service.py ./compose/local/flask/entrypoint \
./compose/local/flask/start  /
COPY ./compose/local/flask/celery/worker/start /start-celeryworker
COPY ./compose/local/flask/celery/beat/start /start-celerybeat
WORKDIR /usr/src/app
ENTRYPOINT ["/entrypoint"]
