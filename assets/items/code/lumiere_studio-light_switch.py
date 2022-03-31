if not ("DSLR" in game.active_map.items.values()):
    game.active_map.place_item("Picture 1/6", game)
    game.active_map.place_item("Picture 2/6", game)
    game.active_map.place_item("Picture 3/6", game)
    game.active_map.place_item("Picture 4/6", game)
    game.active_map.place_item("Picture 5/6", game)
    game.active_map.place_item("Picture 6/6", game)

    game.active_map.fmt[[12, 1, 12, 1, 5, 7], [10, 12, 43, 46, 50, 50]] = "ﯦ"
    game.active_map.place_item("DSLR", game)
    game.active_map.place_item("Side Quest 3", game)

    game.active_map.fmt[[1, 3, 4, 1, 1, 2, 3, 6, 7, 7],[57, 57, 57, 59, 61, 66, 66, 66, 66, 64]] = ["","ﲟ"," ", " ", "ﲟ", "", "", "", "", ""]

else:
    game.active_map.remove_item("Picture 1/6", game)
    game.active_map.remove_item("Picture 2/6", game)
    game.active_map.remove_item("Picture 3/6", game)
    game.active_map.remove_item("Picture 4/6", game)
    game.active_map.remove_item("Picture 5/6", game)
    game.active_map.remove_item("Picture 6/6", game)

    game.active_map.fmt[[12, 1, 12, 1, 5, 7], [10, 12, 43, 46, 50, 50]] = ""
    game.active_map.remove_item("DSLR", game)
    game.active_map.remove_item("Side Quest 3", game)

    game.active_map.fmt[[1, 3, 4, 1, 1, 2, 3, 6, 7, 7],[57, 57, 57, 59, 61, 66, 66, 66, 66, 64]] = " "