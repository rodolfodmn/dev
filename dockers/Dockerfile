FROM ubuntu:16.04
MAINTAINER Rodolfo rodolfo.dmn@gmail.com
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    curl \
    make 
RUN apt install -y ssh 
RUN apt-get install software-properties-common
RUN add-apt-repository 'deb http://archive.ubuntu.com/ubuntu trusty universe'
RUN apt-get install -y python-software-properties
RUN add-apt-repository -y ppa:ondrej/php
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C
RUN apt update
RUN apt install -y php5.6 php5.6-json php5.6-xml php5.6-mysql php5.6-mcrypt 
RUN apt install libapache2-mod-php5.6
RUN a2enmod rewrite
RUN service apache2 restart
EXPOSE 80 443
