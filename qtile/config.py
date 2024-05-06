# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from colors import layout_colorscheme as colorscheme
from colors import layout_theme, dmenu_command, dmenu_kill_process_command, dmenu_emoji_command

from common import slash_powerline_right, slash_powerline_left
from common import arrow_powerline_right, arrow_powerline_left
from common import status_commands
from common import groups_fns

mod = "mod4"
alt = "mod1"
# terminal = guess_terminal()
terminal = "tabbed -c -r 2 st -w \'\' -t \"Simple Termnial\""

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    # Key([mod], ",", lazy.next_screen(), desc="Move cursor to the next screen"),
    # Key([mod], ".", lazy.next_screen(), desc="Move cursor to the next screen"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Key([mod, "shift"], "h", lazy.function(groups_fns.window_to_prev_group), desc="Move to previous group"),
    # Key([mod, "shift"], "l", lazy.function(groups_fns.window_to_next_group), desc="Move to next group"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key(["control"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    # Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([alt], "f4", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Key([alt], "p", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),
    Key([alt], "p", lazy.spawn(dmenu_command), desc="Spawn a command using a prompt widget"),
    Key([mod, "shift"], "q", lazy.spawn(dmenu_kill_process_command), desc="Kill a process"),
    Key([alt, "control"], "space", lazy.spawn(dmenu_emoji_command), desc="Choose an emoji to copy to your clipboard"),
    Key([alt], "w", lazy.spawn("prime-run brave"), desc="Spawn browser"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4, insert_position=0),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme, new_client_position="top"),
    layout.Floating(**layout_theme),
    layout.Max(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_font = "Hack Nerd Font"
widget_defaults = dict(
    font=widget_font,
    fontsize=14,
    padding=4,
    background=colorscheme["normal"]["background"]
)
extension_defaults = widget_defaults.copy()

def get_widgets_list():
    return [
        widget.GroupBox(
            font=widget_font,
            highlight_method="line",
            active=colorscheme["select"]["foreground"],
            foreground=colorscheme["select"]["foreground"],
            inactive=colorscheme["normal"]["foreground"],
            # highlight_color="#ff0000",#colorscheme["select"]["border"],
            # block_highlight_text_color="#ff0000",#colorscheme["select"]["background"],
            this_screen_border=colorscheme["select"]["border"],
            this_current_screen_border=colorscheme["select"]["border"],
            other_current_screen_border=colorscheme["select"]["other-border"],
            other_screen_border=colorscheme["select"]["other-border"],
            visible_groups=[],
        ),
        widget.WindowName(
            font=widget_font,
            background = colorscheme["normal"]["background"],
            foreground = colorscheme["select"]["foreground"],
            ),
        # widget.TaskList(
        #     icon_size = 15,
        #     font = widget_font,
        #     foreground = colorscheme["select"]["foreground"],
        #     background = colorscheme["select"]["background"],
        #     borderwidth = 0,
        #     border = colorscheme["normal"]["border"],
        #     margin = 0,
        #     padding = 8,
        #     highlight_method = "block",
        #     title_width_method = "uniform",
        #     urgent_alert_method = "border",
        #     urgent_border = colorscheme["select"]["border"],
        #     rounded = False,
        #     txt_floating = "🗗 ",
        #     txt_maximized = "🗖 ",
        #     txt_minimized = "🗕 ",
        # ),
        widget.Systray(
            foreground=colorscheme["normal"]["foreground"],
            background=colorscheme["normal"]["background"],
            ),
        widget.TextBox("|", 
            name="delimiter",
            foreground=colorscheme["normal"]["foreground"],
            background=colorscheme["normal"]["background"],
        ),
        widget.KeyboardLayout(
            configured_keyboards=["us", "ro"],
            display_map={"us": " en", "ro": " ro"},
            font=widget_font,
            foreground=colorscheme["normal"]["foreground"],
            background=colorscheme["normal"]["background"],
            ),
        widget.TextBox("|", 
            name="delimiter",
            font=widget_font,
            foreground=colorscheme["normal"]["foreground"],
            background=colorscheme["normal"]["background"],
        ),
        widget.Battery(
            # format=" {percent:2.0%}",
            format=status_commands.get_battery_percentage(),
            font=widget_font,
            foreground = colorscheme["normal"]["foreground"],
            background = colorscheme["normal"]["background"],
        ),
        widget.TextBox("|", 
            name="delimiter",
            font=widget_font,
            foreground=colorscheme["normal"]["foreground"],
            background=colorscheme["normal"]["background"],
        ),
        widget.Clock(
            # format=" %a %d %b %Y %H:%M:%S",
            format = status_commands.get_date_time(),
            font=widget_font,
            foreground=colorscheme["normal"]["foreground"],
            background=colorscheme["normal"]["background"]
        ),
        widget.TextBox("|", 
            name="delimiter",
            font=widget_font,
            foreground=colorscheme["normal"]["foreground"],
            background=colorscheme["normal"]["background"],
        ),
        widget.CurrentLayoutIcon(
            scale = 0.7,
            font=widget_font,
            foreground = colorscheme["select"]["foreground"],
            background = colorscheme["normal"]["background"],
        ),
    ]

def get_secondary_widgets_list():
    secondary_panel = get_widgets_list()
    # remove system tray
    del secondary_panel[2:4]
    return secondary_panel
        
screens = [
    Screen(
        top=bar.Bar(
            widgets=get_widgets_list(),
            size=24,
            background=colorscheme["normal"]["background"],
            margin=5,
            ),
    ),
    Screen(
        top=bar.Bar(
            widgets=get_secondary_widgets_list(),
            size=24,
            background=colorscheme["normal"]["background"],
            margin=5,
            ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
