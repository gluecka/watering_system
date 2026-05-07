#!/bin/bash

# This file is created to start the defined mode 
# - Summer Mode --> --profile summer
# - Winter Mode --> --profile winter

# Delete the # to define the mode !!!!!!


# !!!!!!!!! Summer Mode !!!!!!!!!!!

docker compose -f docker-compose.service.yml --profile summer up -d

# !!!!!!!!!!!! Winter Mode !!!!!!!!!!!


# docker compose -f docker-compose.service.yml --profile summer kill
# docker rm -f py-trigger
# docker rm -f py-data_wathering
# docker compose -f docker-compose.service.yml --profile winter up -d