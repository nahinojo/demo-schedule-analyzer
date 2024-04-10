FROM python:3

ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=1.8.2

RUN curl -sSL https://install.python-poetry.org | python3 -
COPY /api /api
WORKDIR /api
RUN poetry install $(test "$YOUR_ENV" == production && echo "--only=main") --no-interaction --no-ansi
WORKDIR ..

EXPOSE 5000

CMD python /api/run.py