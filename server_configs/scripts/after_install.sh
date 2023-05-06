#!/usr/bin/env bash

# Install libaries
cd /home/ubuntu/quebook-new-aws
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --no-input

# Set permission for all files
sudo chown -R www-data:www-data /home/ubuntu/quebook-new-aws
sudo chmod 755 /home/ubuntu

# Restart services
sudo service apache2 restart