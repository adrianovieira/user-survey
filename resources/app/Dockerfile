FROM node:22.16-alpine AS builder

WORKDIR /usr/src/app

COPY ./code/surveys-status-1.0/ .

RUN npm install
RUN npm run build

FROM node:22.15-alpine AS api

WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/dist .
COPY --from=builder /usr/src/app/node_modules ./node_modules

EXPOSE 8000

ENTRYPOINT [ "node","app.js" ]
