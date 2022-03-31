game.map("Lumiere Studio").remove_item("Side Quest 3", game)

game.active_map.fmt[[6, 6], [48, 49]] = " "
game.active_map.fmt_ref[[6, 6], [48, 49]] = " "

message = "-door opens-\n Such weak security, tch tch..."
sg.popup_no_buttons(message, auto_close = True, auto_close_duration = 2, no_titlebar = True, modal = True,  background_color = "#4D4D4D", keep_on_top = True)
