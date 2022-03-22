game.surface("░").walkable = True
message = f"You can now walk on {game.surface('░').name} (░)!"

sg.popup_no_buttons(message, auto_close = True, auto_close_duration = 2, no_titlebar = True, modal = True,  background_color = "#4D4D4D", keep_on_top = True)
