game.map("Atal Mukherjee's Shop").remove_item("Pay", game)

game.pocket.append(game.item("Mop"))

game.map("Biswas Office").remove_item("CV", game)
game.map("Biswas Office").place_item("Find PhD", game)

sg.popup_no_buttons("You have bought a mop.", auto_close = True, auto_close_duration = 2, no_titlebar = True, modal = True,  background_color = "#4D4D4D", keep_on_top = True)

game.map("Atal Mukherjee's Shop").remove_item("Atal Mukherjee (Expectant)", game)
game.map("Atal Mukherjee's Shop").place_item("Atal Mukherjee (Tired)", game)
