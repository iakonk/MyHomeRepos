#!/bin/sh

if [ -O $PGDATA/PG_VERSION ]
then
  echo $PGDATA/PG_VERSION 'exists and is owned by the effective user ID: ' $(whoami)
else
  sudo --non-interactive /bin/chown --recursive postgres:postgres $PGDATA
  sudo --non-interactive /bin/chmod --recursive --verbose 0700 $PGDATA
fi

sudo --non-interactive /bin/chown --recursive postgres:postgres $PGBACKUP
sudo --non-interactive /bin/chmod --recursive --verbose 0700 $PGBACKUP

if [ -e $PGDATA/PG_VERSION ]
then
  echo 'Database has been already initialized'
else
    /usr/lib/postgresql/11/bin/initdb
fi
/usr/lib/postgresql/11/bin/postgres -c config_file=/etc/postgresql/postgresql.conf