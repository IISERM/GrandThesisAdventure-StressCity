game.surface("┅").walkable = ~game.surface("┅").walkable

message = f"Secret entrance is unlocked!" if(game.surface('┅').walkable) else f"Secret entrance is locked."

sg.popup_no_buttons(message, auto_close = True, auto_close_duration = 2, no_titlebar = True, modal = True,  background_color = "#4D4D4D", keep_on_top = True)
