FROM python:3.7-alpine3.9

ADD ./informatyka /app/.informatyka
WORKDIR /app/.informatyka
RUN mv informatyka.sh /usr/bin/commit
RUN chmod 777 /usr/bin/commit
RUN mv init.sh /usr/bin/init
RUN chmod 777 /usr/bin/init
RUN apk update && \
    apk upgrade && \
    apk add git zip