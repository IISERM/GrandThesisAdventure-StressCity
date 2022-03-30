message = ""

if not ("Wrench" in game.pocket.itemlist):
    message = "I need to find a wrench somewhere around here..."
    game.active_map.place_item("Wrench", game)

elif (game.active_map.fmt[29,131] == "⎢"):
    message = "...-CREAAAAK-...\nThat did the trick!"
    game.active_map.fmt[[28, 29, 30], [131, 131, 131]] = "→"
    game.active_map.fmt_ref[[28, 29, 30], [131, 131, 131]] = "→"

    game.active_map.remove_item("Jammed door", game)

sg.popup_no_buttons(message, auto_close = True, auto_close_duration = 2, no_titlebar = True, modal = True,  background_color = "#4D4D4D", keep_on_top = True)
