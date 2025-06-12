FROM postgres:16-alpine AS pg-server

RUN apk update \
    && apk add --no-cache postgresql-timescaledb \
    && apk cache clean --purge