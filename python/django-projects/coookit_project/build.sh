#!/bin/bash

function clean_up() {
    echo 'Cleaning up images'

    if [ -z $(docker ps --all --quiet | head -1) ]
      then
          echo 'no containers to remove'
      else
          # at least one container was found, removing them all
          docker rm --force $(docker ps --quiet --all --no-trunc)
    fi
    if [ -z $(docker images --quiet | head -1) ]
      then
          echo 'no images to remove'
      else
          # at least one image was found, removing them all
          docker rmi --force $(docker images --quiet --no-trunc)
    fi
    echo '==========================================================='
}

function build_images() {
    echo 'Building docker images'
    docker build \
          --force-rm \
          --build-arg DEV="1" \
          --build-arg UWSGI_CHDIR=/home/coookit \
          --build-arg DJANGO_SETTINGS_MODULE=coookit.settings \
          --build-arg PYTHONPATH=/usr/local/lib/python3.7/dist-packages/ \
          --file docker/app/Dockerfile \
          --tag coookit-app-img .
    echo '==========================================================='
}

function start_app_locally() {
    docker run -d \
          --name coookit-app \
          --volume $PWD:/home \
          --volume $PWD/uploads:/app/uploads \
          --publish "8080:8080" \
          coookit-app-img
    echo '==========================================================='
}


# main section
# exit as soon as exit code -eq 1
set -e
clean_up
make package
build_images
start_app_locally
make clean

