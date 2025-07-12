# Commands
alias vi="nvim"
alias svi="sudo vim"
alias python="python3"
alias go="grc go"
alias ranger=". ranger"
alias lf="lfcd"
#alias gimp="env GTK2_RC_FILES=/usr/share/themes/Sweet-Dark/gtk-2.0/gtkrc GTK_DATA_PREFIX= gimp-2.10"
alias start-minidlna="minidlnad -f ${HOME}/.config/minidlna/minidlna.conf -P ${HOME}/.config/minidlna/minidlna.pid -d"
alias reload-minidlna="minidlnad -f ${HOME}/.config/minidlna/minidlna.conf -R"
alias steam-offload="prime-offload && prime-run steam"
alias show-orphane-packages="sudo pacman -Qtdq"
alias remove-orphane-packages="sudo pacman -Qtdq | sudo pacman -Rns -"
alias tabbed-zathura="tabbed -c zathura -e"


# Change Directories
alias suckless-dir="cd ${HOME}/.config/suckless"
alias dwm-dir="cd ${HOME}/.config/suckless/dwm"
alias dmenu-dir="cd ${HOME}/.config/suckless/dmenu"
alias st-dir="cd ${HOME}/.config/suckless/st"
alias slock-dir="cd ${HOME}/.config/suckless/slock"
alias blocks-dir="cd ${HOME}/.config/suckless/dwmblocks"
alias tabbed-dir="cd ${HOME}/.config/suckless/tabbed"
alias scripts-dir="cd ${HOME}/.config/scripts"
alias work-dir="cd ${HOME}/Documents/Important/Work"
alias manga-dir="cd ${HOME}/Documents/Manga"
alias projects-dir="cd ${HOME}/Documents/Projects"
alias movies-dir="cd /run/media/aldan/Seagate\ Expansion\ Drive/Movies"
alias external-hd-dir="cd /run/media/aldan/Seagate\ Expansion\ Drive"
alias imp-dir="cd ${HOME}/Documents/Important"
alias test-dir="cd ${HOME}/Documents/Test"
alias memes-dir="cd ${HOME}/Pictures/Memes"
alias courses-dir="cd ${HOME}/Documents/Important/OnlineCourses"
alias dotfiles-dir="cd ${HOME}/Documents/Projects/dotfiles"


# Work related
alias kc="kubectl"
alias kb="kubebuilder"

# Yazi
function y() {
	local tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
	yazi "$@" --cwd-file="$tmp"
	if cwd="$(command cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
		builtin cd -- "$cwd"
	fi
	rm -f -- "$tmp"
}
