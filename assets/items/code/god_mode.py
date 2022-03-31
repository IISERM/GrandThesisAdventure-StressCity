# codes = ["ABr", "ABs", "Sawsib", "CAF", "CC", "Gazebo", "SR", "PHD", "Room", "Hostels", "Labyrinth", "SC", "Lata", "LHC", "Road"]
codes = ['abr', 'abs', 'sawsib', 'caf', 'cc', 'gazebo', 'sr', 'phd', 'room', 'hostels', 'labyrinth', 'sc', 'atal', 'lhc', 'road']
areas = ["AB Reception", "AB1 AB2", "Sawsib Office", "CAF", "Community Centre", "Gazebo", "H7 Study Room", "PhD Room", "Hostel Room", "Hostels", "Labyrinth", "SC", "Atal Mukherjee's Shop", "LHC", "Road"]
tp_dict = dict(zip(codes, areas))

lt = [
    [sg.Text("God Mode", justification='center', font='Serif 13', expand_x=True)],
    [sg.Text("Teleport anywhere, at will.\n\nKeys: ['abr', 'abs', 'sawsib', 'caf', 'cc', 'gazebo', 'sr', 'phd', 'room', 'hostels', 'labyrinth', 'sc', 'atal', 'lhc', 'road']", size=(50, None))],
    [sg.Input(key="in", size=(50, None))],
    [sg.Button("Close", expand_x=True),
    sg.Button("Submit", expand_x=True, bind_return_key=True)]
]

win = sg.Window("Found an item!", layout=lt, modal=True, keep_on_top=True, finalize=True)
win.bind("<Escape>", "Close")
while True:
    event,v = win.read()
    if event=="Submit":
        map_to = win["in"].get().lower()
        if (map_to in tp_dict.keys()):
            win["in"].update(background_color="#004f00")
            sg.popup_no_buttons("Teleporting!", auto_close = True, auto_close_duration = 1, no_titlebar = True, modal = True,  background_color = "#4D4D4D")
            win["in"].update(value = "", background_color="#4d4d4d")
            game.active_map = game.map(tp_dict[map_to])
            game.active_map.pos = game.active_map.init_pos
            break
        else:
            win["in"].update(value = "", background_color="#6b0618")
            sg.popup_no_buttons("Invalid input!", auto_close = True, auto_close_duration = 1, no_titlebar = True, modal = True,  background_color = "#4D4D4D")
            win["in"].update(value = "", background_color="#4d4d4d")

    elif event=="Close" or event==sg.WIN_CLOSED:
        break
    else:
        break
win.close()
