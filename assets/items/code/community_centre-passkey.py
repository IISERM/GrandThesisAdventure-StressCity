message = ""

if (game.active_map.fmt[37, 43] == "─"):
    message = "...-BEEEEP-...\nThe door has opened!"
    game.active_map.fmt[[37, 37, 37], [43, 44, 45]] = " "
    game.active_map.fmt_ref[[37, 37, 37], [43, 44, 45]] = " "

    game.active_map.remove_item("Pass Key", game)

sg.popup_no_buttons(message, auto_close = True, auto_close_duration = 2, no_titlebar = True, modal = True,  background_color = "#4D4D4D", keep_on_top = True)
