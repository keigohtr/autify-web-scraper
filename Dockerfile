FROM python:3.8 AS production

COPY ./pyproject.toml /app/pyproject.toml
COPY ./poetry.toml /app/poetry.toml
COPY ./poetry.lock /app/poetry.lock

RUN pip install pip -U \
    && pip install poetry \
    && cd /app \
    && poetry install --no-dev \
    && pip uninstall poetry -y

COPY . /app
WORKDIR /app

ENV PYTHONPATH /app


FROM production AS development

RUN pip install poetry \
    && cd /app \
    && poetry install