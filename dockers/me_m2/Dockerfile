FROM ubuntu:16.04
RUN apt-get update
RUN apt install -y software-properties-common
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php
RUN add-apt-repository 'deb http://archive.ubuntu.com/ubuntu trusty universe'
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE77A6C
RUN apt-get update
RUN apt-get install -y \
	build-essential \
	automake \
	pkg-config \
	libevent-dev \
	libncurses5-dev \
	pv \
	wget \
	language-pack-en \
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
	zsh \
	make

RUN apt install -y \
	php7 \
	php7-gd \
	php7-json \
	libapache2-mod-php7 \
	php7-curl \
	php7-xml \
	php7-mysql \
	php7-mcrypt \
	php7-zip php7-soap php7-mbstring php7-xdebug php7-intl

RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
RUN curl -sS https://getcomposer.org/installer -o /tmp/composer-setup.php
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') === 'e5325b19b381bfd88ce90a5ddb7823406b2a38cff6bb704b0acc289a09c8128d4a8ce2bbafcd1fcbdc38666422fe2806') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
RUN php /tmp/composer-setup.php --install-dir=/usr/local/bin --filename=composer
RUN curl -sL https://deb.nodesource.com/setup_12.x -o /tmp/nodesource_setup.sh
RUN bash /tmp/nodesource_setup.sh
RUN apt install nodejs -y
RUN mkdir ~/.npm-global
RUN npm config set prefix '~/.npm-global'

RUN gem install compass
RUN a2enmod rewrite
RUN mkdir -p /var/www/html/stores
RUN chmod 777 /var/www/html -R
RUN service apache2 restart
ADD start.sh /home/rods/start.sh
RUN chmod +x /home/rods/start.sh
RUN useradd -m rods && echo "rods:root" | chpasswd && adduser rods sudo
RUN chown rods:rods -R /home/rods
USER rods

ENTRYPOINT /home/rods/start.sh && /bin/bash
EXPOSE 22 80 443
