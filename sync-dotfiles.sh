#!/bin/bash

# Variables
DOTFILES_DIR="$( dirname -- "$( readlink -f -- "$0"; )"; )"
HOME_DIR="${HOME}"
CONFIG_DIR="${HOME_DIR}/.config"

# Sync folders
function sync_terminals() {
    ln -sf "${DOTFILES_DIR}/alacritty" "${CONFIG_DIR}/alacritty"
    ln -sf "${DOTFILES_DIR}/kitty" "${CONFIG_DIR}/kitty"
}

function defaults(){
    ln -sf "${DOTFILES_DIR}/mimeapps/mimeapps.list" "${CONFIG_DIR}/mimeapps.list"
    ln -sf "${DOTFILES_DIR}/qt5ct" "${CONFIG_DIR}/qt5ct"
    ln -sf "${DOTFILES_DIR}/xorg/.Xresources" "${HOME_DIR}/.Xresources"
    ln -sf "${DOTFILES_DIR}/xorg/.xinitrc" "${HOME_DIR}/.xinitrc"
}

function window_managers(){
    ln -sf "${DOTFILES_DIR}/qtile" "${CONFIG_DIR}/qtile"
    ln -sf "${DOTFILES_DIR}/awesome" "${CONFIG_DIR}/awesome"
    ln -sf "${DOTFILES_DIR}/hypr" "${CONFIG_DIR}/hypr"
    ln -sf "${DOTFILES_DIR}/i3" "${CONFIG_DIR}/i3"
    ln -sf "${DOTFILES_DIR}/i3blocks" "${CONFIG_DIR}/i3blocks"
}

function shells() {
    ln -sf "${DOTFILES_DIR}/shells/.bashrc" "${HOME_DIR}/.bashrc"
    ln -sf "${DOTFILES_DIR}/shells/.zshrc" "${HOME_DIR}/.zshrc"

    ln -sf "${DOTFILES_DIR}/shells/.zprofile" "${HOME_DIR}/.zprofile"
    ln -sf "${DOTFILES_DIR}/shells/.bash_profile" "${HOME_DIR}/.bash_profile"

    ln -sf "${DOTFILES_DIR}/shells/.bash_aliases" "${HOME_DIR}/.bash_aliases"
    ln -sf "${DOTFILES_DIR}/shells/zsh" "${CONFIG_DIR}/zsh"
}

function emacs() {
    # ln -sf "${DOTFILES_DIR}/emacs" "${CONFIG_DIR}/emacs"
    ln -sf "${DOTFILES_DIR}/doom" "${CONFIG_DIR}/doom"
}

function common() {
    ln -sf "${DOTFILES_DIR}/ranger" "${CONFIG_DIR}/ranger"
    ln -sf "${DOTFILES_DIR}/lf" "${CONFIG_DIR}/lf"
    ln -sf "${DOTFILES_DIR}/sxiv" "${CONFIG_DIR}/sxiv"
    ln -sf "${DOTFILES_DIR}/lsd" "${CONFIG_DIR}/lsd"
    ln -sf "${DOTFILES_DIR}/htop" "${CONFIG_DIR}/htop"
    ln -sf "${DOTFILES_DIR}/btop" "${CONFIG_DIR}/btop"
    ln -sf "${DOTFILES_DIR}/GIMP" "${CONFIG_DIR}/GIMP"
    ln -sf "${DOTFILES_DIR}/minidlna" "${CONFIG_DIR}/minidlna"
    ln -sf "${DOTFILES_DIR}/mpv" "${CONFIG_DIR}/mpv"
    ln -sf "${DOTFILES_DIR}/fastfetch" "${CONFIG_DIR}/fastfetch"
    ln -sf "${DOTFILES_DIR}/dunst" "${CONFIG_DIR}/dunst"
    ln -sf "${DOTFILES_DIR}/flameshot" "${CONFIG_DIR}/flameshot"
    ln -sf "${DOTFILES_DIR}/zathura" "${CONFIG_DIR}/zathura"
    ln -sf "${DOTFILES_DIR}/pcmanfm" "${CONFIG_DIR}/pcmanfm"
    ln -sf "${DOTFILES_DIR}/picom" "${CONFIG_DIR}/picom"
    ln -sf "${DOTFILES_DIR}/vlc" "${CONFIG_DIR}/vlc"
    ln -sf "${DOTFILES_DIR}/tmux" "${CONFIG_DIR}/tmux"
    ln -sf "${DOTFILES_DIR}/nitrogen" "${CONFIG_DIR}/nitrogen"
}

function main() {
    sync_terminals
    defaults
    window_managers
    shells
    emacs
    common
}

main
