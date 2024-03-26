#!/bin/ash
python manage.py migrate blog  
python manage.py migrate
python manage.py runserver 127.0.0.1:8000