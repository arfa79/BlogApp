#!/bin/bash

# Apply migrations for the 'blog' app
python manage.py migrate blog

# Apply all other migrations
python manage.py migrate
# Create superuser for authentication
python manage.py createsuperuser
# Run server
python manage.py runserver 127.0.0.1:8000