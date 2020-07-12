FROM ubuntu:16.04
RUN apt-get update
RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:ondrej/php
RUN add-apt-repository 'deb http://archive.ubuntu.com/ubuntu trusty universe'
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C
RUN apt-get update
RUN apt-get install -y \
    build-essential \
    automake \
    pkg-config \
    libevent-dev \
    libncurses5-dev \
    pv \
    wget \
    vim \
    git \
    gcc \
    ssh \
    curl \
    apache2 \
    sudo \
    ruby-full \
	locales \
    php \
    make

RUN apt install -y \
    php5.6 \
    php5.6-gd \
    php5.6-json \
    libapache2-mod-php5.6 \
    php5.6-curl \
    php5.6-xml php5.6-mysql php5.6-mcrypt php5.6-zip php5.6-soap php5.6-mbstring php5.6-xdebug php5.6-intl

RUN curl -sL https://deb.nodesource.com/setup_12.x -o ~/nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt install nodejs
RUN mkdir ~/.npm-global
RUN npm config set prefix '~/.npm-global'

RUN gem install compass
RUN a2enmod rewrite
RUN mkdir -p /var/www/html/stores
RUN chmod 777 /var/www/html -R
RUN service apache2 restart
ADD start.sh /home/rods/start.sh
RUN chmod +x /home/rods/start.sh
RUN useradd -m rods && echo "rods:rods" | chpasswd && adduser rods sudo
RUN chown rods:rods -R /home/rods
ENTRYPOINT /home/rods/start.sh && /bin/bash
EXPOSE 22 80 443
