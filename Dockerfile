FROM python:3.10-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /usr/src/app

RUN apt update -y \
    && apt install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    wait-for-it \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install poetry

RUN poetry install

EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]