FROM python:3.6.8-alpine

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    jpeg-dev zlib-dev libjpeg \
    && pip install --no-cache-dir psycopg2 \
    && pip install --no-cache-dir psycopg2-binary \
    && pip install Pillow \
    && apk del --no-cache .build-deps

WORKDIR /online_store

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT gunicorn online_store.wsgi:application -w 2 -b :8000
