FROM ubuntu:22.04

WORKDIR /app

COPY package*.json ./

RUN apt-get update && \
    apt-get install -y nodejs npm && \
    npm install && \
    npm cache clean --force && \
    apt-get purge -y --auto-remove npm && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.npm && \
    rm -rf /tmp/*

COPY . .

CMD ["node", "index.js"]