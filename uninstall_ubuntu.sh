#!/bin/bash

# app web
echo Disinstallazione applicazione web...
pip3 uninstall -y setuptools
pip3 uninstall -y html5lib flask flask-sqlalchemy selenium bs4
apt remove --purge --yes python3-pip

# nginx reverse proxy
echo Disinstallazione del reverse proxy...
apt remove --purge --yes nginx
rm /etc/nginx/nginx.conf
rm -r /etc/nginx/ssl/

echo Disinstallazione completata.
