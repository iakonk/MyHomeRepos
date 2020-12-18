FROM ubuntu:18.04

ENV TZ=Europe/Kiev \
    DEBIAN_FRONTEND=noninteractive \
    PACKAGES="\
        curl \
        ca-certificates \
        gnupg \
        sudo \
    " \
    PG_PACKAGES="\
        postgresql-11 \
        postgresql-client-11 \
        postgresql-contrib-11 \
    "

RUN apt update \
  && apt -y install $PACKAGES \
  && curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
  && echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" > /etc/apt/sources.list.d/pgdg.list \
  && apt update \
  && apt -y install $PG_PACKAGES \
  && apt-get clean

COPY --chown=postgres:postgres etc/postgresql.conf etc/pg_hba.conf /etc/postgresql/
COPY --chown=postgres:postgres docker/db/init.sql docker/db/entrypoint.sh ./
COPY docker/db/postgres /etc/cron.daily/postgres

RUN chmod +x ./entrypoint.sh \
  && echo 'postgres ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers \
  && chmod 0755 /etc/cron.daily/postgres

USER postgres

RUN /etc/init.d/postgresql start

ENTRYPOINT ["./entrypoint.sh"]