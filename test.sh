#!/bin/sh
docker-compose -f ./$1/docker-compose.yml up --force-recreate --build --abort-on-container-exit
