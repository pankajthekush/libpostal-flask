#!/bin/bash

# deployment script on cloud
git clone https://github.com/pankajthekush/libpostal-flask.git /home/ubuntu/libpostal-flask
cd /home/ubuntu/libpostal-flask
docker-compose up --scale lpostal=4

