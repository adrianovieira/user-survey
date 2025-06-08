FROM node:22.16-alpine AS builder

WORKDIR /usr/src/app

COPY ./code/backend/ .

RUN npm install
RUN npm run build

FROM node:22.15-alpine AS api

WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/dist .
COPY --from=builder /usr/src/app/node_modules ./node_modules

ENV API_PORT=8000

EXPOSE ${API_PORT}

ENTRYPOINT [ "node","app.js" ]
