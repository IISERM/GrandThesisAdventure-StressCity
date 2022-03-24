import PySimpleGUI as sg
game.active_map.remove_item("X Marks The Spot!", game)
game.active_map.place_item("X Marks The Spot", game)

yogiPopupLayout = [
            [sg.Text("The Voice", justification='center', font='Serif 13', expand_x=True)],
            [sg.Text("faceless.yogi@gmail.com", size=(50, None))],
            [],
            [sg.Button("Close", expand_x=True)]
        ]
yogiPopup = sg.Window("There's a message from heaven", layout=yogiPopupLayout, modal=True, keep_on_top=True, finalize=True)
yogiPopup.bind("<Escape>", "Close")
while True:
    e, v = yogiPopup.read()
    if e == "Close":
        break
yogiPopup.close()