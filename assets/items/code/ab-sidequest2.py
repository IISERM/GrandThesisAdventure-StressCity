game.map("AB1 AB2").remove_item("Side Quest 2", game)

message = "-CLUNKKK- Ohhhhhh shit, did I break it??\n\n -picks up a broken piece- \n\nBetter get out of here. (⊙_⊙;)"

sg.popup_no_buttons(message, auto_close = True, auto_close_duration = 3.5, no_titlebar = True, modal = True,  background_color = "#4D4D4D", keep_on_top = True)

game.map("AB1 AB2").remove_item("Side Quest 2", game)
game.pocket.append(game.item("Broken Antenna"))