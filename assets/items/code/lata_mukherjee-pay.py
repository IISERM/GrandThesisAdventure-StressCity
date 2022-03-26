game.map("Lata Mukherjee's Shop").remove_item("Pay", game)
game.active_map.exits["0,36"] = ["SC",[48,63]]
game.active_map.exit_coords.append([0,36])

game.map("Biswas Office").remove_item("CV", game)
game.map("Biswas Office").place_item("Find PhD", game)