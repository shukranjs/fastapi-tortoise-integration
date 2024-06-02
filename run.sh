#!/bin/bash

# Stop and remove existing containers
docker-compose down

# Build the Docker image
docker-compose build

# Start the Docker containers
docker-compose up -d
