#!/bin/sh
pip install -r requirements.txt
python manage.py migrate --run-syncdb
python manage.py create_admin
