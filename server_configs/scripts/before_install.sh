#!/usr/bin/env bash
sudo -s
sudo apt-get update
sudo apt-get install -y python3 python-dev python3-pip apache2 libapache2-mod-wsgi-py3
pip install --root --upgrade virtualenv
sudo rm -rf /var/www/html