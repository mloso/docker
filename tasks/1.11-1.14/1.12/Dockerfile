FROM node:16-alpine

WORKDIR /app

COPY package.json .

RUN npm install

COPY example-frontend .

ENV REACT_APP_BACKEND_URL=http://localhost:8080

CMD ["npm", "start"]
