FROM ubuntu:18.04

ENV TZ=Europe/Kiev \
    DEBIAN_FRONTEND=noninteractive

RUN apt update && apt -y install curl ca-certificates gnupg ;\
    curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - ;\
    echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" > /etc/apt/sources.list.d/pgdg.list ;\
    apt update && apt -y install postgresql-11 postgresql-client-11 postgresql-contrib-11

COPY --chown=postgres:postgres etc/postgresql.conf /etc/postgresql/
COPY --chown=postgres:postgres etc/init.sql ./

USER postgres

RUN /etc/init.d/postgresql start &&\
    psql --file ./init.sql

CMD ["/usr/lib/postgresql/11/bin/postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]