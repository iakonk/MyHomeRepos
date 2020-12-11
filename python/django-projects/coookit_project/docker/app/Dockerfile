FROM python:2

ARG DEV
ARG DJANGO_SETTINGS_MODULE
ARG UWSGI_CHDIR
ARG PYTHONPATH
ARG PG_HOST
ARG PG_PORT
ARG PG_USER
ARG PG_PASS
ARG PG_DB_NAME
ENV DEV=$DEV \
    DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE \
    UWSGI_CHDIR=$UWSGI_CHDIR \
    PYTHONPATH=$PYTHONPATH \
    PG_HOST=$PG_HOST \
    PG_PORT=$PG_PORT \
    PG_USER=$PG_USER \
    PG_PASS=$PG_PASS \
    PG_DB_NAME=$PG_DB_NAME \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1  \
    PACKAGES="\
        nginx \
        python-setuptools \
    "

WORKDIR /app

RUN echo 'deb [arch=amd64] http://nginx.org/packages/mainline/ubuntu/ bionic nginx' >> /etc/apt/sources.list.d/nginx.list \
    && echo 'deb-src http://nginx.org/packages/mainline/ubuntu/ bionic nginx' >> /etc/apt/sources.list.d/nginx.list \
    && wget http://nginx.org/keys/nginx_signing.key \
    && apt-key add nginx_signing.key \
    && apt update \
    && apt install -y $PACKAGES \
    && apt-get clean \
    && find /etc/nginx/conf.d -name '*.conf' -delete \
    && easy_install pip \
    && pip install --upgrade pip

COPY requirements.txt Makefile dist/coookit-*.tar.gz docker/app/entrypoint.sh ./

RUN useradd coookit \
    && mkdir -p /app/static \
                /app/cache \
                /var/run/supervisor \
                /var/run/uwsgi \
                /var/run/nginx \
                /var/log/supervisor \
                /var/log/nginx \
                /var/log/uwsgi \
                /var/log/django \
                /var/cache/nginx \
    && chown --recursive coookit:coookit /var/log/uwsgi \
                                         /var/log/django \
                                         /var/log/nginx \
                                         /var/run/uwsgi \
                                         /var/run/nginx \
                                         /var/cache/nginx \
    && chmod +x ./entrypoint.sh

COPY --chown=coookit:coookit etc/nginx.conf etc/supervisord.conf etc/uwsgi.ini /app/etc/
COPY docker/app/uwsgi docker/app/django /etc/logrotate.d/

EXPOSE 8080

ENTRYPOINT ["/app/entrypoint.sh"]