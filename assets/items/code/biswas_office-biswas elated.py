sg.popup_no_buttons("Ughh... What a fantastic start of my masters thesis. Troubles keep finding me.", auto_close = True, auto_close_duration = 2, no_titlebar = True, modal = True,  background_color = "#4D4D4D", keep_on_top = True)

if("Lata Mukherjee (Idle)" in game.map("Lata Mukherjee's Shop").items.values()):
    game.map("Lata Mukherjee's Shop").remove_item("Lata Mukherjee (Idle)", game)
    game.map("Lata Mukherjee's Shop").place_item("Lata Mukherjee (Expectant)", game)

