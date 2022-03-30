game.surface("┅").walkable = ~game.surface("┅").walkable

message = f"Secret entrance is unlocked!" if(game.surface('┅').walkable) else f"Secret entrance is locked."

sg.popup_no_buttons(message, auto_close = True, auto_close_duration = 2, no_titlebar = True, modal = True,  background_color = "#4D4D4D", keep_on_top = True)


labyrinthEndPopupLayout = [
            [sg.Text("You have solved the Labyrinth.", justification='center', font='Serif 13', expand_x=True)],
            [sg.Text("Share a screenshot of this popup with the organizers. If you are the first team to reach here, you will win.", size=(50, None))],
            [],
            [sg.Button("Close", expand_x=True)]
        ]
labyrinthPopup = sg.Window("Well Done", layout=labyrinthEndPopupLayout, modal=True, keep_on_top=True, finalize=True)
labyrinthPopup.bind("<Escape>", "Close")
while True:
    e, v = labyrinthPopup.read()
    if e == "Close" or "WIN-CLOSED":
        break
labyrinthPopup.close()