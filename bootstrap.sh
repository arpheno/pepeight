#!/bin/sh -e
sudo apt-get -y update
sudo apt-get -y install python-pip vim  npm curl git
sudo ln -s /usr/bin/nodejs /usr/bin/node
sudo npm install -g bower vulcanize
sudo pip install pytest-django pytest-xdist coverage
sudo pip install -r /vagrant/requirements.txt
cd /vagrant/backendfail/
bower install --allow-root
python manage.py migrate
