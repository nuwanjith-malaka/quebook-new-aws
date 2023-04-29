#!/usr/bin/env bash

# Install libaries
cd /var/www/html/quebook-new-aws
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --no-input

# Set permission for all files
sudo chown -R www-data:www-data /var/www/html/quebook-new-aws

# Restart services
sudo service apache2 restart