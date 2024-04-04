#!/bin/bash
echo "Running Django migrations..."
python qr_app/manage.py makemigrations
python qr_app/manage.py migrate

echo "Starting Django server..."
python qr_app/manage.py runserver
