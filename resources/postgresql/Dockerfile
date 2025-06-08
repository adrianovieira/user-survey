FROM postgres:14-alpine AS pg-server

RUN apk update \
    && apk add --no-cache postgresql-timescaledb \
    && apk cache clean --purge