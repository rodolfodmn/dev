echo 'cirando ambiente de desenvolvimento maroto :D'
mkdir dbs
mkdir modules
mkdir -p html/stores
git clone https://github.com/rodolfodmn/dotfiles
git clone https://github.com/rodolfodmn/py_bash.git
git clone https://github.com/rodolfodmn/php_bash.git
git clone https://github.com/rodolfodmn/bash
git clone https://github.com/rodolfodmn/magentoTinyFixes
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

cp ./utils/.tern-project ~/
cp ./dotfiles/.tmux.conf ~/
cp ./dotfiles/.zshrc ~/
cp ./dotfiles/.vimrc ~/
cp ./dotfiles/.bashrc ~/

