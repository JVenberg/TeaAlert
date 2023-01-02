FROM node:19.3-slim

WORKDIR /app

COPY package.json package.json

RUN npm install

COPY . /app

CMD npm start