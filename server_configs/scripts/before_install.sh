#!/usr/bin/env bash
sudo apt-get update
sudo apt-get install -y python3 python-dev python3-pip python3-venv apache2 libapache2-mod-wsgi-py3
pip install --ubuntu --upgrade virtualenv
sudo rm -rf /home/ubuntu/quebook-new-aws