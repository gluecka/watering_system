#!/bin/bash

docker run -d --privileged=true --name=soil_ident --restart=always ghcr.io/gluecka/ident:1.0
