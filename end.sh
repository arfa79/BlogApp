#!/bin/bash
# Remove pgdata volume for the related container 
sudo rm -rf pgdata
# Creating pgdata folder again for next time build
mkdir pgdata
docker-compose down 