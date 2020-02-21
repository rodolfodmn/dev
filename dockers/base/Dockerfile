FROM ubuntu:16.04
RUN apt-get update
RUN apt install -y software-properties-common
RUN add-apt-repository 'deb http://archive.ubuntu.com/ubuntu trusty universe'
RUN add-apt-repository ppa:neovim-ppa/stable
RUN apt-get update
RUN apt-get install -y \
    build-essential \
    pv \
    neovim \
    git \
    gcc \
    ssh \
    curl \
    apache2 \
    sudo \
    make

RUN a2enmod rewrite
RUN service apache2 restart
ADD start.sh /home/rods/start.sh
RUN chmod +x /home/rods/start.sh
RUN useradd -m rods && echo "rods:rods" | chpasswd && adduser rods sudo
RUN chown rods:rods -R /home/rods
ENTRYPOINT /home/rods/start.sh && bash
EXPOSE 80 443
