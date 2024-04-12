FROM node:21-alpine as client

COPY /client /client
WORKDIR /client
RUN npm install .
RUN npm run build
WORKDIR ..

FROM python:3
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY /api /api
COPY --from=client /api/app/static/bundle.js /api/app/static/bundle.js

WORKDIR /api
RUN poetry install --no-interaction --no-ansi

WORKDIR ..
EXPOSE 5000
CMD python /api/run.py