FROM python:3.10 AS apiI2

RUN pip install --upgrade --no-cache-dir pip pipenv

COPY Pipfile.lock Pipfile ./

RUN useradd --create-home worker \
    && pipenv install --system --deploy --ignore-pipfile \
    && pipenv --clear \
    && rm -f Pipfile.lock Pipfile

USER worker

WORKDIR /home/worker

ENV PATH="/home/worker/.local/bin:${PATH}"

COPY --chown=worker:worker code/surveys-status-1.2/ ./src/app/

EXPOSE 8000

CMD ["sh", "-c", "ddtrace-run uvicorn fastapi_main:app --host 0.0.0.0 --port 8281  --workers ${APP_WORKERS}"]