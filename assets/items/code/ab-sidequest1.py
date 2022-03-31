game.map("AB1 AB2").remove_item("Side Quest 1 Answer?", game)
game.map("Community Centre").remove_item("Side Quest 1", game)

message = "You have found a banana!"
sg.popup_no_buttons(message, auto_close = True, auto_close_duration = 2, no_titlebar = True, modal = True,  background_color = "#4D4D4D", keep_on_top = True)

game.pocket.append(game.item("Banana"))
