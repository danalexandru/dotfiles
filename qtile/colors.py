from pathlib import Path

# Colorschemes
default = {
    "normal": {
        "background": "#222222",
        "foreground": "#bbbbbb",
        "border": "#444444",
        "other-bolder": "#404040",
    },
    "select": {
        "background": "#005577",
        "foreground": "#eeeeee",
        "border": "#005577",
        "other-botder": "#404040",
    }
}


doom_one = {
    "normal": {
        "background": "#14191F",
        "foreground": "#8C92AC",
        "border": "#14191F",
        "other-boder": "#c678dd",
    },
    "select": {
        "background": "#1F2833",
        "foreground": "#F3F3F6",
        "border": "#0087ff",
        "other-border": "#c678dd",
    }
}


gruvbox = {
    "normal": {
        "background": "#282828",
        "foreground": "#ebdbb2",
        "border": "#282828",
        "other-boder": "#458588",
    },
    "select": {
        "background": "#1d2021",
        "foreground": "#ffaf00",
        "border": "#ffaf00",
        "other-border": "#458588",
    }
}

# breeze_dark = {
#     "normal": {
#         "background": "#2a2e32",
#         "foreground": "#eff0f1",
#         "border": "#2a2e32"
#     },
#     "select": {
#         "background": "#1b1e20",
#         "foreground": "#eff0f1",
#         "border": "#3daee9"
#     }
# }

# Layouts
layout_colorscheme = gruvbox
layout_theme = {
        "margin":5,
        "border_width": 2,
        "border_focus": layout_colorscheme["select"]["border"],
        "border_normal": layout_colorscheme["normal"]["border"],
        "border_focus_stack": layout_colorscheme["select"]["border"],
        "border_normal_stack": layout_colorscheme["normal"]["border"]
}

# Dmenu
dmenu_command = ("dmenu_run -nb %s -nf %s -sb %s -sf %s -p \"%s\"" % (layout_colorscheme["normal"]["background"], layout_colorscheme["normal"]["foreground"], layout_colorscheme["select"]["background"], layout_colorscheme["select"]["foreground"], "dmenu run:"))
dmenu_kill_process_command = ("%s/.config/scripts/dmenu/dmenu-kill-process.sh --%s" % (Path.home(), "gruvbox"))
dmenu_emoji_command = ("%s/.config/scripts/dmenu/dmenu-emoji.sh --%s" % (Path.home(), "gruvbox"))
	# { MODKEY|ShiftMask,             XK_q,      spawn,          SHCMD("~/.config/scripts/dmenu/dmenu-kill-process.sh --gruvbox") },
	# { ALTKEY|ControlMask,           XK_space,  spawn,          SHCMD("~/.config/scripts/dmenu/dmenu-emoji.sh --gruvbox") },
