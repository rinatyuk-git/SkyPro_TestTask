FROM python:3.11.9-slim

WORKDIR /app

# Copy only the file with dependencies
COPY pyproject.toml poetry.lock ./

RUN pip install --upgrade pip && \
    apt-get update && \
    apt-get -y install gcc

# Install Poetry and dependencies
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-root

COPY . .
