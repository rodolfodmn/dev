echo "hello rods ;D"
passwd rods
gem install compass
apt install -y mysql-server-5.6
add-apt-repository -y ppa:ondrej/php
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C
apt update
apt install -y \
    php5.6 \
    php5.6-gd php5.6-json php5.6-curl php5.6-xml php5.6-mysql php5.6-mcrypt php5.6-zip php5.6-soap php5.6-mbstring php5.6-xdebug php5.6-intl

apt install -y libapache2-mod-php5.6
# cd ~
# wget https://github.com/neovim/neovim/releases/download/v0.4.3/nvim.appimage
# ./nvim.appimage --appimage-extract
# cp ~/squashfs-root/usr/* /usr -r

#Install node 12 <
curl -sL https://deb.nodesource.com/setup_12.x -o ~/nodesource_setup.sh
bash nodesource_setup.sh
apt install nodejs
#Install node 12 >

#npm user config <
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
#npm user config >

vim /etc/apache2/apache2.conf
vim /etc/apache2/sites-available/default-ssl.conf 
vim /etc/apache2/sites-available/000-default.conf
mkdir -p /var/www/html/stores
chmod 777 /var/www/html -R
sudo service apache2 restart
