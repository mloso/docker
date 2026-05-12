FROM node:16-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install && \
    npm cache clean --force && \
    rm -rf /root/.npm && \
    rm -rf /tmp/*

COPY . .

CMD ["npm", "start"]