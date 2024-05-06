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
}

function main() {
    sync_terminals
    defaults
    window_managers
    shells
    common
}

main
