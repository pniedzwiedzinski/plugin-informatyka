FROM python:3.7-alpine3.9

RUN apk update && \
    apk upgrade && \
    apk add --no-cache git zip

WORKDIR /app

ADD ./informatyka /app/


RUN mv informatyka.sh /usr/bin/commit
RUN mv init.sh /usr/bin/init
