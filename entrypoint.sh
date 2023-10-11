#!/bin/sh

# Apply database migrations
flask db upgrade

# Run the command passed in docker-compose or Dockerfile
gunicorn app:app --bind 0.0.0.0:5001
