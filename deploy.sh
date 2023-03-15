#!/bin/bash

# deployment script on cloud
docker network create xtnet
pull docker.io/pkumdev/libpostal-flask:v1
git clone https://github.com/pankajthekush/libpostal-flask.git /home/ubuntu/libpostal-flask
cd /home/ubuntu/libpostal-flask
docker-compose up --scale lpostal=4

