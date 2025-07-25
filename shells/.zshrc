# Enable colors and change prompt:
autoload -U colors && colors
# Load version control information
autoload -Uz vcs_info
autoload -U compinit

# git_branch() {
#     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/\1/'
# }
# 
# PROMPT="%B%{$fg[green]%}[%n%{$fg[yellow]%}@%{$fg[cyan]%}%m:%{$fg[red]%}%c %{$fg[magenta]%}($(git_branch))%f%{$fg[green]%}] %{$fg[yellow]%}%% %{$reset_color%}%b"

zstyle ':vcs_info:*' enable git
zstyle ':vcs_info:*' formats "%b"

precmd() { vcs_info }
setopt prompt_subst
stty stop undef		# Disable ctrl-s to freeze terminal.

PROMPT='%B%{$fg[green]%}[%n%{$fg[yellow]%}@%{$fg[cyan]%}%m:%{$fg[red]%}%c %{$fg[magenta]%}(${vcs_info_msg_0_})%f%{$fg[green]%}] %{$fg[yellow]%}%% %{$reset_color%}%b'

# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
setopt autocd
bindkey -e

# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '${HOME}/.zshrc'

# Basic auto/tab complete:
zstyle ':completion:*' menu select
zstyle ':completion:*' list-colors 'di=34:ln=35:so=32:pi=33:ex=31:bd=46;34:cd=43;34:su=41;30:sg=46;30:tw=42;30:ow=43;30'
alias ls="ls --color=auto"

zmodload zsh/complist
compinit
_comp_options+=(globdots)	

# # Load zsh-syntax-highlighting; should be last.
# source zsh-autocomplete.plugin.zsh 2>/dev/null

if [ -f ~/.bash_aliases ]; then
  . ~/.bash_aliases
fi

# Add directories to path
SCRIPTS_DIR="${HOME}/.config/scripts"
HOME_BIN="${HOME}/bin"
RUBY_BIN="${HOME}/.local/share/gem/ruby/3.0.0/bin"
GO_BIN="${HOME}/go/bin"
LOCAL_BIN="${HOME}/.local/bin"
DOOM_EMACS_BIN="${HOME}/.config/emacs/bin"
PATH=$PATH:$SCRIPTS_DIR:$HOME_BIN:$RUBY_BIN:$GO_BIN:$LOCAL_BIN:$DOOM_EMACS_BIN


# Configure Kubernetes autocomplete
autoload -U +X compinit && compinit
autoload -U +X bashcompinit && bashcompinit

source <(kubectl completion zsh)
complete -F __start_kubectl kc


alias grep="grep --color=auto"
# alias ls="colorls"
alias ls="lsd"
#
# exports
export KUBE_EDITOR=nvim
export VISUAL=nvim
export EDITOR=nvim

bindkey "^[[1;3C" forward-word
bindkey "^[[1;3D" backward-word

# chpwd() {exec zsh}

# source ~/.config/zsh/zsh-vi-mode/zsh-vi-mode.zsh
source ~/.config/zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/.config/zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
# source ~/.config/zsh/zsh-autocomplete/zsh-autocomplete.plugin.zsh

source ~/.manpage.sh

# colorscript --random

# eval "$(zoxide init --cmd cd zsh)"
#
LFCD="${HOME}/.config/lf/lfcd.sh"
if [ -f "$LFCD" ]; then
    source "$LFCD"
fi
autoload -Uz compinit && compinit
