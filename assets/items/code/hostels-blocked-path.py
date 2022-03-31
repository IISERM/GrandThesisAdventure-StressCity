message = ""

if not ("Shovel" in game.active_map.items.values() or "Shovel" in game.pocket.itemlist):
    message = "I should probably visit this later.."
elif not ("Shovel" in game.pocket.itemlist):
    message = "This must be the lumiere photo-booth. I wonder if there's a shovel somewhere around here.."
elif (game.active_map.fmt[0,561] == "▉"):
    message = "...-THUNK- -THUNK- -THUNK-...\nPhew, the path is cleared!"
    game.active_map.fmt[[0, 0, 0], [560, 561, 562]] = "↑"
    game.active_map.fmt_ref[[0, 0, 0], [560, 561, 562]] = "↑"

    game.active_map.remove_item("Blocked Path", game)

sg.popup_no_buttons(message, auto_close = True, auto_close_duration = 2, no_titlebar = True, modal = True,  background_color = "#4D4D4D", keep_on_top = True)
