#!/bin/sh

# Programs to run
udiskie &
flameshot & 
numlockx &
dunst &
# nm-applet &

# Other
#~/.config/scripts/multimonitor_layout.sh
#~/.config/scripts/multimonitor_layout2.sh
# ~/.config/scripts/multimonitor_layout3.sh

xrdb -load ~/.Xresources
nitrogen --restore

setxkbmap -layout us,ro -option grp:alt_shift_toggle

# dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY
${HOME}/.config/scripts/toggle-transparency.sh &
# ${HOME}/.screenlayout/layout-ct.sh
${HOME}/.screenlayout/layout-b.sh
${HOME}/.config/suckless/dwmblocks/dwmblocks &

xset s off
xset -dpms
xset s noblank

# Turn CapsLock off
setxkbmap -option ctrl:nocaps &

# Turn CapsLock back on
# setxkbmap -option (to turn back on)

# Make file picker dialogue work on chromium
systemctl --user import-environment DISPLAY XAUTHORITY

exec dwm
# exec awesome
# exec qtile start
# exec i3
