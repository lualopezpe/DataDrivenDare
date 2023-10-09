#!/bin/sh

# Apply database migrations
flask db upgrade

# Run the command passed in docker-compose or Dockerfile
exec "$@"
