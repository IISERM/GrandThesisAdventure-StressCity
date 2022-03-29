sg.popup_no_buttons("Ughh... What a fantastic start of my masters thesis. Troubles keep finding me.", auto_close = True, auto_close_duration = 2, no_titlebar = True, modal = True,  background_color = "#4D4D4D", keep_on_top = True)

if("Atal Mukherjee (Idle)" in game.map("Atal Mukherjee's Shop").items.values()):
    game.map("Atal Mukherjee's Shop").remove_item("Atal Mukherjee (Idle)", game)
    game.map("Atal Mukherjee's Shop").place_item("Atal Mukherjee (Expectant)", game)

