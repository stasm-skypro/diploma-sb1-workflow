#!/bin/bash

# Ожидаем, пока база будет доступна
echo "Waiting for postgres..."

while ! nc -z $DB_HOST 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

# Запускаем Celery
echo "Starting Celery worker..."
celery -A config worker --loglevel=info
