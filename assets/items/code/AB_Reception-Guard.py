for i in game.maps:
    if i.name == "biswas_office":
        map = i
# game.active_map.pos = [10, 10]
print(map)
game.active_map = map