FROM debian:12.1-slim

ENV PYTHONUNBUFFERED=1
ENV NODE_ENV=production

RUN apt-get update -y \
    && apt-get install -y \
        dumb-init vim curl \
        python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /workspace/src \
    && curl -sSL https://install.python-poetry.org | python3 - --version 1.6.1
# set poetry path
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /workspace
COPY pyproject.toml poetry.lock /workspace/

RUN poetry install

# Set up migrations
# COPY ./yoyo.ini /workspace/yoyo.ini

COPY ./src /workspace/src/

ENTRYPOINT [ "dumb-init", "--" ]

CMD [ "poetry", "run", "python3", "src/main.py" ]

