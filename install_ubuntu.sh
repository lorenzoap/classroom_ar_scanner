#!/bin/bash

# app web
echo Installazione applicazione web...
apt install --yes python3.8 python3-pip # python3-dev build-essential
# pip3 install --upgrade pip wheel # Per risolvere un problema durante la compilazione di uwsgi
pip3 install setuptools
pip3 install html5lib flask flask-sqlalchemy selenium bs4

# nginx reverse proxy
echo Installazione del reverse proxy...
apt install --yes nginx
cp ./Proxy/nginx.conf /etc/nginx/nginx.conf
mkdir /etc/nginx/ssl/
cp ./Proxy/cas.key /etc/nginx/ssl/cas.key
cp ./Proxy/cas.crt /etc/nginx/ssl/cas.crt
systemctl reload nginx

echo Installazione completata. Per avviare il server, eseguire lo script "run.sh".
