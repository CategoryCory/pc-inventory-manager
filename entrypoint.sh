#!/bin/bash
set -e

python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput
exec gunicorn --bind 0.0.0.0:8000 pc_inventory_manager.wsgi:application