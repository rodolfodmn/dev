echo 'cirando ambiente de desenvolvimento maroto pro docker'
mkdir -p ~/.config/nvim
cp ./html/sql_para_lojas_gitlab.sql ./dbs
cp ./html/adminer.php ./html/stores
cat ./dotfiles/zshrc  > ~/.zshrc
cp ./dotfiles/init.vim ~/.config/nvim
cat ./dotfiles/bashrc > ~/.bashrc

