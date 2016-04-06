#! /bin/sh

apt-get install nginx -y
service nginx start
update-rc.d nginx defaults
service nginx stop
service nginx start
mkdir /etc/nginx/sites-available
mkdir /etc/nginx/sites-enabled
mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bkp
cp ./extras/nginx/nginx.conf /etc/nginx/nginx.conf
cp ./extras/nginx/sites-available/app /etc/nginx/sites-available/app
ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app

apt-get install virtualenv -y
virtualenv ./walmart --python=python2.7 --no-site-packages
