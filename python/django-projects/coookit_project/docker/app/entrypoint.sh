#!/bin/sh

su - coookit -c "cd /app && make database"
supervisord -c /app/etc/supervisord.conf