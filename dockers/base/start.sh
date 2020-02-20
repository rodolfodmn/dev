echo "hello rods ;D"
passwd rods
apt install -y mysql-server-5.6
add-apt-repository -y ppa:ondrej/php
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C
apt update
apt install -y php5.6 php5.6-json php5.6-curl php5.6-xml php5.6-mysql php5.6-mcrypt php5.6-zip
apt install -y libapache2-mod-php5.6
nvim /etc/apache2/apache2.conf
nvim /etc/apache2/sites-available/default-ssl.conf 
nvim /etc/apache2/sites-available/000-default.conf
mkdir -p /var/www/html/stores
chmod 777 /var/www/html -R
sudo service apache2 restart