FROM debian:12.1-slim

ENV PYTHONUNBUFFERED=1
ENV NODE_ENV=production

RUN apt-get update -y \
    && apt-get install -y \
        dumb-init vim curl \
        nodejs npm \
    && rm -rf /var/lib/apt/lists/*

# set poetry path
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /workspace
COPY package.json package-lock.json /workspace/

RUN npm install --omit=dev

COPY ./src /workspace/src/

ENTRYPOINT [ "dumb-init", "--" ]

CMD [ "node", "src/main.js" ]

