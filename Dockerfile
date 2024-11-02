FROM python:3.10-alpine

# Instala utilidades adicionales en Alpine
RUN apk add --no-cache shadow

# Setea variables de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    CRYPTOGRAPHY_DONT_BUILD_RUST=1 \
    POETRY_VERSION=1.8.2

RUN pip3 install --upgrade pip setuptools wheel poetry==${POETRY_VERSION}

# Configura Poetry
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    POETRY_HOME=/opt/poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

# Construye las dependencias usando buildkit cache mounts
RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install

COPY ./src/ /app/

# Crea grupo y usuario para ejecutar la aplicación
RUN groupadd -g 700 gym && useradd -g gym gym && chown gym:gym -R /app
USER gym

EXPOSE 8000
CMD [""]
