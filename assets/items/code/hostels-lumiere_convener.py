if not ("Shovel" in game.active_map.items.values() or "Shovel" in game.pocket.itemlist):
    game.map("Hostels").place_item("Shovel", game)
elif ("DSLR" in game.pocket.itemlist):
    game.map("Hostels").remove_item("Lumiere Convener", game)
    game.map("Hostels").place_item("Lumiere Convener (Happy)", game)
