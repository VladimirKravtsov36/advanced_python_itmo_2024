FROM python:3.12-slim-bullseye

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
    texlive-full \
    pandoc \
    ; \
    rm -rf /var/lib/apt/lists/*
