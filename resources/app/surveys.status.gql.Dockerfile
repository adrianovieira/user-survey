FROM python:3.13-alpine AS gql

RUN pip install --upgrade --no-cache-dir pip pipenv

COPY code/surveys-status-gql/Pipfile.lock ./
COPY code/surveys-status-gql/Pipfile ./

RUN adduser -D worker \
    && pipenv install --system --deploy --ignore-pipfile \
    && pipenv --clear \
    && rm -f Pipfile.lock Pipfile

USER worker

WORKDIR /home/worker

ENV PATH="/home/worker/.local/bin:${PATH}"

ENV PYTHONPATH=/home/worker

COPY --chown=worker:worker code/surveys-status-gql/src/app/ ./app/

EXPOSE 8000

CMD ["sh", "-c", "fastapi run app/gql.py --host 0.0.0.0 --port 8000 "]