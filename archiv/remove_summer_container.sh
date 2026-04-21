#!/bin/bash

# docker compose -f docker-compose.service.yml --profile summer kill
docker rm -f py-trigger & docker rm -f py-data_wathering
