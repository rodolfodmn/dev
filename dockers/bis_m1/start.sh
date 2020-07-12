#!/bin/bash

if [ -z "$1" ]; then
    if [ "$1" == 'new' ]; then
        echo "iniciando uma nova imagem!";
        passwd rods
        apt install -y mysql-server-5.6

        vim /etc/apache2/apache2.conf
        vim /etc/apache2/sites-available/default-ssl.conf 
        vim /etc/apache2/sites-available/000-default.conf
    fi
fi
