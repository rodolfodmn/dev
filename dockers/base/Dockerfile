FROM ubuntu:16.04
RUN apt-get update
RUN apt install -y software-properties-common
RUN add-apt-repository 'deb http://archive.ubuntu.com/ubuntu trusty universe'
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
    make

RUN locale-gen en_US.UTF-8
RUN a2enmod rewrite
RUN service apache2 restart
ADD start.sh /home/rods/start.sh
RUN chmod +x /home/rods/start.sh
RUN useradd -m rods && echo "rods:rods" | chpasswd && adduser rods sudo
RUN chown rods:rods -R /home/rods
ENTRYPOINT /home/rods/start.sh && /bin/bash
EXPOSE 22 80 443
