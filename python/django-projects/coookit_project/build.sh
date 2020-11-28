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
    docker-compose up --remove-orphans --always-recreate-deps --force-recreate
    echo '==========================================================='
}

# main section
clean_up
make package
build_images
make clean

