message = ""

if not ("Key" in game.pocket.itemlist):
    message = "I need to find a key somewhere around here..."
    game.active_map.place_item("Key", game)

elif (game.active_map.fmt[182,17] == "─"):
    message = "...-CLICK-...\nThat did the trick!"
    game.active_map.fmt[[182, 182, 182], [16, 17, 18]] = " "
    game.active_map.fmt_ref[[182, 182, 182], [16, 17, 18]] = " "

    game.active_map.remove_item("Locked Cage", game)

sg.popup_no_buttons(message, auto_close = True, auto_close_duration = 2, no_titlebar = True, modal = True,  background_color = "#4D4D4D", keep_on_top = True)
