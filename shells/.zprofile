#
# ~/.zprofile
#

[[ -f ~/.zshrc ]] && . ~/.zshrc

# if [[ "$(tty)" = "/dev/tty1" ]]; then
#     pgreg dwm || startx
# fi

export QT_QPA_PLATFORMTHEME="qt5ct" 
alias grep='grep --color=auto'

# export MOZ_ENABLE_WAYLAND=1
export MOZ_DISABLE_RDD_SANDBOX=1
export MOZ_X11_EGL=1
# export XDG_CURRENT_DESKTOP='X-Generic'
# export MOZ_WEBRENDER=0
# systemctl --user import-environment DISPLAY XAUTHORITY
