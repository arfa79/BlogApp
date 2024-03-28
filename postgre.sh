#!/bin/bash

# Apply migrations for the 'blog' app
python manage.py migrate blog

# Apply all other migrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver 127.0.0.1:8000