#!/bin/bash
# Install dependencies
python -m pip install -r requirements.txt

# Run database migrations to update the schema
python manage.py makemigrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput