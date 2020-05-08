#!/bin/bash

# app web
echo Disinstallazione applicazione web...
apt remove --purge --yes python3.8 python3-pip # python3-dev build-essential
# pip3 install --upgrade pip wheel # Per risolvere un problema durante la compilazione di uwsgi
pip3 uninstall setuptools
pip3 uninstall html5lib flask flask-sqlalchemy selenium bs4

# nginx reverse proxy
echo Disinstallazione del reverse proxy...
apt remove --purge --yes nginx
rm /etc/nginx/nginx.conf
rm -r /etc/nginx/ssl/

echo Disinstallazione completata.