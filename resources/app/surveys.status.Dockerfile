FROM python:3.13-alpine AS api-i2

RUN pip install --upgrade --no-cache-dir pip pipenv

COPY code/surveys-status-1.2/Pipfile.lock ./
COPY code/surveys-status-1.2/Pipfile ./

RUN adduser -D worker \
    && pipenv install --system --deploy --ignore-pipfile \
    && pipenv --clear \
    && rm -f Pipfile.lock Pipfile

USER worker

WORKDIR /home/worker

ENV PATH="/home/worker/.local/bin:${PATH}"

COPY --chown=worker:worker code/surveys-status-1.2/src/app/ ./app/

EXPOSE 8000

CMD ["sh", "-c", "fastapi run app/api.py --host 0.0.0.0 --port 8000 "]