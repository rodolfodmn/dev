echo 'cirando ambiente de desenvolvimento maroto :D'
mkdir dbs
mkdir modules
mkdir -p html/stores
mkdir -p ~/.config/nvim
git clone https://github.com/rodolfodmn/dotfiles
git clone https://github.com/rodolfodmn/py_bash.git
git clone https://github.com/rodolfodmn/php_bash.git
git clone https://github.com/rodolfodmn/bash
git clone https://github.com/rodolfodmn/magentoTinyFixes

cp ./html/sql_para_lojas_gitlab.sql ./dbs
cp ./html/adminer.php ./html/stores
cp ./dotfiles/.zshrc ~/
cp ./dotfiles/init.vim ~/.config/nvim
cp ./dotfiles/.bashrc ~/

