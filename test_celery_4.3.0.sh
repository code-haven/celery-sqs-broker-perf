#!/bin/sh
docker-compose -f ./celery4.3.0/docker-compose.yml up --force-recreate --build --abort-on-container-exit
