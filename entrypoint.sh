#!/bin/sh

# Wait for PostgreSQL to be available
while ! nc -z db 5432; do
  echo "Waiting for PostgreSQL..."
  sleep 1
done

# Run Aerich migrations

aerich init -t config.TORTOISE_ORM
aerich init-db
aerich migrate
aerich upgrade
# Start FastAPI server
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
