#!/bin/sh

# apply migrations
poetry run python manage.py migrate

# start applications
poetry run python manage.py runserver 0.0.0.0:8000