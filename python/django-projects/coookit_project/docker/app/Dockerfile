FROM python:3

ARG DJANGO_SETTINGS_MODULE
ARG UWSGI_CHDIR
ARG PYTHONPATH
ENV DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE \
    UWSGI_CHDIR=$UWSGI_CHDIR \
    PYTHONPATH=$PYTHONPATH \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN mkdir -p /app/static \
             /app/cache \
             /app/uploads \
             /var/run/supervisor \
             /var/run/uwsgi \
             /var/run/nginx \
             /var/log/supervisor \
             /var/log/nginx \
             /var/log/uwsgi \
             /var/log/django \
             /var/cache/nginx

RUN echo 'deb [arch=amd64] http://nginx.org/packages/mainline/ubuntu/ bionic nginx' >> /etc/apt/sources.list.d/nginx.list ;\
    echo 'deb-src http://nginx.org/packages/mainline/ubuntu/ bionic nginx' >> /etc/apt/sources.list.d/nginx.list ;\
    wget http://nginx.org/keys/nginx_signing.key &&\
    apt-key add nginx_signing.key &&\
    apt update && \
    apt install -y nginx  &&\
    apt-get clean &&\
    find /etc/nginx/conf.d -name '*.conf' -delete

RUN useradd coookit

COPY --chown=coookit:coookit etc /app/etc
COPY requirements.txt Makefile dist/coookit-*.tar.gz ./

RUN make install &&\
    chown --recursive coookit:coookit /var/log/uwsgi ;\
    chown --recursive coookit:coookit /var/log/django ;\
    chown --recursive coookit:coookit /var/log/nginx ;\
    chown --recursive coookit:coookit /var/run/uwsgi ;\
    chown --recursive coookit:coookit /var/run/nginx ;\
    chown --recursive coookit:coookit /var/cache/nginx ;\
    chown --recursive coookit:coookit /app ;\
    chmod --recursive g+s /app ;\
    chmod --recursive g+s /var/log/uwsgi ;\
    chmod --recursive g+s /var/log/nginx ;\
    chmod --recursive g+s /var/log/django ;\
    rm -f ./requirements.txt ./Makefile ./coookit-*.tar.gz ./nginx_signing.key

EXPOSE 8080

CMD ["supervisord", "-c", "/app/etc/supervisord.conf"]