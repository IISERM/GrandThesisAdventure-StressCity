game.map("Lata Mukherjee's Shop").place_item("Pay", game)
del game.active_map.exits["0,36"]
game.active_map.exit_coords.remove([0,36])