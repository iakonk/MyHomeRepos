#!/bin/sh

chown -R coookit:coookit /app
chmod g+s /app/uploads
cd /app && make database

supervisord -c /app/etc/supervisord.conf