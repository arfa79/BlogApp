#!/bin/bash
sudo rm -rf pgdata
mkdir pgdata
docker-compose down 
docker rmi $(docker images | grep 'blogapp') redis:7.2.4-alpine postgres:14.1-alpine