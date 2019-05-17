FROM python:3.7-alpine3.9

RUN apk --update add --no-cache git zip && \
    rm -rf /var/cache/apk/*

RUN echo "alias git='git --git-dir=/app/git'" >> /etc/profile.d/git.sh


ADD ./informatyka /app/

WORKDIR /app/informatyka

RUN mv ../informatyka.sh /usr/bin/commit
RUN mv ../init.sh /usr/bin/init
