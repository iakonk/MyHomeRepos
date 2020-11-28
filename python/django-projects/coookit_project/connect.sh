#!/bin/bash

if [ "$1" == "app" ]; then
    IMG_NAME="coookit-app-img"
fi
if [ "$1" == "db" ]; then
    IMG_NAME="coookit-db-img"
fi
if [ -z "$1" ] || [ -z "$IMG_NAME" ]; then
    echo "No arguments were provided. Valid arguments are: [app|db]"
    exit 1
fi

id=$(docker ps --quiet --filter "ancestor=$IMG_NAME")
echo 'container id: ' $id
docker exec -it `echo $id` /bin/bash
