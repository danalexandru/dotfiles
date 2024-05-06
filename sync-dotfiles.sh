#!/bin/bash

# Variables
SCRIPT_DIR="$( dirname -- "$( readlink -f -- "$0"; )"; )"
HOME_DIR="${HOME}"
CONFIG_DIR="${HOME_DIR}/.config"

# Sync folders
function sync_terminals() {
    ln -sf "${SCRIPT_DIR}/alacritty" "${CONFIG_DIR}/alacritty"
    ln -sf "${SCRIPT_DIR}/kitty" "${CONFIG_DIR}/kitty"
}

function defaults(){
    ln -sf "${SCRIPT_DIR}/mimeapps/mimeapps.list" "${CONFIG_DIR}/mimeapps.list"
    ln -sf "${SCRIPT_DIR}/xorg/.Xresources" "${HOME_DIR}/.Xresources"
    ln -sf "${SCRIPT_DIR}/xorg/.xinitrc" "${HOME_DIR}/.xinitrc"
}

function window_managers(){
    ln -sf "${SCRIPT_DIR}/qtile" "${CONFIG_DIR}/qtile"
    ln -sf "${SCRIPT_DIR}/awesome" "${CONFIG_DIR}/awesome"
    ln -sf "${SCRIPT_DIR}/hypr" "${CONFIG_DIR}/hypr"
    ln -sf "${SCRIPT_DIR}/i3" "${CONFIG_DIR}/i3"
    ln -sf "${SCRIPT_DIR}/i3blocks" "${CONFIG_DIR}/i3blocks"
}

function shells() {
    ln -sf "${SCRIPT_DIR}/shells/.bashrc" "${HOME_DIR}/.bashrc"
    ln -sf "${SCRIPT_DIR}/shells/.zshrc" "${HOME_DIR}/.zshrc"

    ln -sf "${SCRIPT_DIR}/shells/.zprofile" "${HOME_DIR}/.zprofile"
    ln -sf "${SCRIPT_DIR}/shells/.bash_profile" "${HOME_DIR}/.bash_profile"

    ln -sf "${SCRIPT_DIR}/shells/.bash_aliases" "${HOME_DIR}/.bash_aliases"
    ln -sf "${SCRIPT_DIR}/shells/zsh" "${CONFIG_DIR}/zsh"
}

function common() {
    ln -sf "${SCRIPT_DIR}/ranger" "${CONFIG_DIR}/ranger"
    ln -sf "${SCRIPT_DIR}/lf" "${CONFIG_DIR}/lf"
    ln -sf "${SCRIPT_DIR}/sxiv" "${CONFIG_DIR}/sxiv"
    ln -sf "${SCRIPT_DIR}/lsd" "${CONFIG_DIR}/lsd"
    ln -sf "${SCRIPT_DIR}/htop" "${CONFIG_DIR}/htop"
    ln -sf "${SCRIPT_DIR}/btop" "${CONFIG_DIR}/btop"
    ln -sf "${SCRIPT_DIR}/GIMP" "${CONFIG_DIR}/GIMP"
    ln -sf "${SCRIPT_DIR}/minidlna" "${CONFIG_DIR}/minidlna"
    ln -sf "${SCRIPT_DIR}/mpv" "${CONFIG_DIR}/mpv"
    ln -sf "${SCRIPT_DIR}/fastfetch" "${CONFIG_DIR}/fastfetch"
    ln -sf "${SCRIPT_DIR}/dunst" "${CONFIG_DIR}/dunst"
    ln -sf "${SCRIPT_DIR}/flameshot" "${CONFIG_DIR}/flameshot"
    ln -sf "${SCRIPT_DIR}/zathura" "${CONFIG_DIR}/zathura"
    ln -sf "${SCRIPT_DIR}/pcmanfm" "${CONFIG_DIR}/pcmanfm"
    ln -sf "${SCRIPT_DIR}/picom" "${CONFIG_DIR}/picom"
}

function main() {
    sync_terminals
    defaults
    window_managers
    shells
    common
}

main
