#!/bin/bash
# set -x  # Разкомментировать для вывода отладочной информации

# Ожидаем, пока база будет доступна
echo "Waiting for postgres..."

while ! nc -z $DB_HOST 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

# Создаём директорию staticfiles с нужными правами
mkdir -p /app/staticfiles
chmod -R 777 /app/staticfiles

# Применяем миграции
echo "Apply migrations from web..."
python manage.py migrate
echo "Migrations applied"


# Загружаем фикстуры (однократно — с проверкой существования пользователей)
echo "Creating admin group..."
python manage.py create_admin_group
echo "Loading fixtures..."
python manage.py load_initial_user_data
python manage.py load_initial_bulletin_data
echo "Fixtures loaded"

# Собираем статику
echo "Собираем статику..."
python manage.py collectstatic --noinput

# Запускаем Gunicorn
echo "Запускаем Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000
