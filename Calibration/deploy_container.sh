#!/bin/bash

docker run -d --privileged=true --name=soil_ident --restart=always ident:1.0
