#!/usr/bin/env bash

# clean codedeploy-agent files and apache for a fresh install
sudo rm -rf /home/ubuntu/install
sudo apt-get purge apache2 

# install CodeDeploy agent
sudo apt-get -y update
sudo apt-get -y install ruby
sudo apt-get -y install wget
cd /home/ubuntu
wget https://aws-codedeploy-us-east-1.s3.amazonaws.com/latest/install
sudo chmod +x ./install 
sudo ./install auto

# update os & install python3
sudo apt-get update
sudo apt-get install -y python3.10 python3.10-dev python3.10-venv python3-pip apache2 libapache2-mod-wsgi-py3
python3 -m pip install --root virtualenv

# delete app
sudo rm -rf /home/ubuntu/quebook-new-aws
