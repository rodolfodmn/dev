#!/bin/bash

echo "iniciando uma nova imagem!";
sudo apt install -y mysql-server-5.6

sudo vim /etc/apache2/apache2.conf
sudo vim /etc/apache2/sites-available/default-ssl.conf 
sudo vim /etc/apache2/sites-available/000-default.conf
#if [ -z "$1" ]; then
	#if [ "$1" == 'new' ]; then
	#fi
#fi
