#!/bin/sh

chown -R coookit:coookit /app
chmod g+s /app/uploads

cd /app
if [ ! -z "$DEV" ]
then
  make dev-install
else
  make prod-install
fi
chown --recursive coookit:coookit /var/log/django

supervisord -c /app/etc/supervisord.conf