import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

from tetra import gadgets
from tetra import terminal
import CustomGadgets

class MyGame(terminal.Game):
    def __init__(self, title, settingsfile, gadgets_list, first_map=None, theme="Dark"):
        super().__init__(title, settingsfile, gadgets_list, first_map, theme)
        self.factsFound = [0 for i in range(15)]

    def bind_sg_events(self):
        super().bind_sg_events()
        self.window.bind("<KeyPress-Up>", "up")
        self.window.bind("<KeyPress-Left>", "left")
        self.window.bind("<KeyPress-Down>", "down")
        self.window.bind("<KeyPress-Right>", "right")

myGame = MyGame("Turing Hunt 2022", "assets/settings.json", [gadgets.Clock, gadgets.GPS, CustomGadgets.StressMeter, CustomGadgets.Phone], "Hostel Room")
myGame.pocket.append(myGame.item("Shoe"))
myGame.pocket.append(myGame.item("God Mode"))
myGame.run()
