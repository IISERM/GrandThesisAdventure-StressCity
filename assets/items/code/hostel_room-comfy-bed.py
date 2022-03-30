game.gadgets[2].val = 75
game.gadgets[2].isActive = False

endGameMsgLayout = [
            [sg.Text("Go To Sleep", justification='center', font='Serif 13', expand_x=True)],
            [sg.Text("You lie down and try to go to sleep. It takes you some time to wind down, and eventually you fall asleep. You have a few nightmares (more than one involving rejection mails,) but overall you get around 9 hours of sleep.\nYou wake up to feel slightly less stressed. You are still stressed, mind you, but you feel braver and better prepared to face the day ahead of you. Life continues to be a roller coaster- Dr. Sawsib never gets back to you and neither does his PhD student.\nAfter a week, Dr. Sawcon accepts to be your thesis advisor. The work you would do in his lab is not exactly what you wanted to do, and he is not known for being very helpful, but his lab does do very innovative work. You expect the coming year to be stressful, but you hope to get some good results in your research and do well in CSIR. Academic life isn't going to be easy, but life goes on, and life goes well...\nMeanwhile, there are still some places in campus you haven't explored. What was behind the jammed door in CAF anyway?", size=(50, None))],
            [],
            [sg.Button("Close", expand_x=True)]
        ]
endGameMsg = sg.Window("The End", layout=endGameMsgLayout, modal=True, keep_on_top=True, finalize=True)
endGameMsg.bind("<Escape>", "Close")
while True:
    e, v = endGameMsg.read()
    if e == "Close" or e == sg.WIN_CLOSED:
        break
endGameMsg.close()