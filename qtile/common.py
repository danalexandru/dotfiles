import datetime, psutil

########## Powerline stuff shamelessly stolen from The Linux Cast ########
from qtile_extras.widget.decorations import PowerLineDecoration
from libqtile.lazy import lazy


arrow_powerline_right = {
    "decorations": [
        PowerLineDecoration(
            path="arrow_right",
            size=11,
        )
    ]
}
arrow_powerline_left = {
    "decorations": [
        PowerLineDecoration(
            path="arrow_left",
            size=11,
        )
    ]
}
rounded_powerline_right = {
    "decorations": [
        PowerLineDecoration(
            path="rounded_right",
            size=11,
        )
    ]
}
rounded_powerline_left = {
    "decorations": [
        PowerLineDecoration(
            path="rouded_left",
            size=11,
        )
    ]
}
slash_powerline_right = {
    "decorations": [
        PowerLineDecoration(
            path="forward_slash",
            size=11,
        )
    ]
}
slash_powerline_left = {
    "decorations": [
        PowerLineDecoration(
            path="back_slash",
            size=11,
        )
    ]
}

class GroupsFns(object):
    def __init__(self, number_of_groups):
        self.number_of_groups = number_of_groups

    @lazy.function
    def window_to_prev_group(self, qtile):
        i = qtile.groups.index(qtile.current_group)
        if qtile.current_window is not None:
            if i > 0:
                qtile.current_window.togroup(qtile.groups[i - 1].name)
                qtile.current_screen.toggle_group(qtile.groups[i - 1])
            else:
                qtile.current_window.togroup(qtile.groups[self.number_of_groups - 1].name)
                qtile.current_screen.toggle_group(qtile.groups[self.number_of_groups - 1])

    @lazy.function
    def window_to_next_group(self, qtile):
        i = qtile.groups.index(qtile.current_group)
        if qtile.current_window is not None:
            if i < self.number_of_groups:
                qtile.current_window.togroup(qtile.groups[i + 1].name)
                qtile.current_screen.toggle_group(qtile.groups[i + 1])
            else:
                qtile.current_window.togroup(qtile.groups[0].name)
                qtile.current_screen.toggle_group(qtile.groups[0])

    
class StatusCommands(object):
    def get_date_time(self):
        hours_icons = ["󱑊", "󱐿", "󱑀", "󱑁", "󱑂", "󱑃", "󱑄", "󱑅", "󱑆", "󱑇", "󱑈", "󱑉", "󱑊"]
        date_icon = ""

        now = datetime.datetime.now()
        hour = now.hour
        if hour > 12:
            hour = hour - 12
        return "{} %a %d %b %Y | {} %H:%M:%S".format(date_icon, hours_icons[hour])
    def get_battery_percentage(self):
        battery_status = {
            "full": "",
            "mostly-full": "",
            "half-full": "",
            "mostly-empty": "",
            "empty": "",
            "error": "",
        }
        charging_icons = {
            "plugged": "ﮣ",
            "unplugged": "ﮤ",
            "error": "",
        }

        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = battery.percent

        battery_status_index = ""
        battery_charging_index = ""
        if percent > 90 and percent <= 100:
            battery_status_index = "full"
        elif percent > 75 and percent <= 90:
            battery_status_index = "mostly-full"
        elif percent > 50 and percent <= 75:
            battery_status_index = "half-full"
        elif percent > 25 and percent <= 50:
            battery_status_index = "mostly-empty"
        elif percent >= 0 and percent <= 25:
            battery_status_index = "empty"
        else:
            battery_status_index = "error"

        if plugged is True:
            battery_charging_index = "plugged"
        elif plugged is False:
            battery_charging_index = "unplugged"
        else:
            battery_charging_index = "error"

        # return "{} % {} {}".format(battery_status[battery_status_index], charging_icons[battery_charging_index], round(percent))
        return " {} {} {}".format(charging_icons[battery_charging_index], battery_status[battery_status_index], "{percent:2.0%}")

status_commands = StatusCommands()
groups_fns = GroupsFns(9)
