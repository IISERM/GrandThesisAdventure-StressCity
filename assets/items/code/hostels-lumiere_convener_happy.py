game.active_map.remove_item("Lumiere Convener (Happy)", game)

# game.pocket.itemlist.remove(game.item("DSLR"))
game.pocket.append(game.item("QR code"))

message = "You give the DSLR, and obtain a QR code."
sg.popup_no_buttons(message, auto_close = True, auto_close_duration = 2, no_titlebar = True, modal = True,  background_color = "#4D4D4D", keep_on_top = True)
