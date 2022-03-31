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


myGame = MyGame("Turing Hunt 2022", "assets/settings.json", [gadgets.Clock, gadgets.GPS, CustomGadgets.StressMeter, CustomGadgets.Phone], "H7 Study Room")

myGame.run()

# Case insensitive; GODMODE keys
# ['abr', 'abs', 'biswas', 'caf', 'cc', 'gazebo', 'sr', 'phd', 'room', 'hostels', 'labyrinth', 'sc', 'lata', 'lhc', 'road']
# ["AB Reception", "AB1 AB2", "Sawsib Office", "CAF", "Community Centre", "Gazebo", "H7 Study Room", "PhD Room", "Hostel Room", "Hostels", "Labyrinth", "SC", "Atal Mukherjee's Shop", "LHC", "Road"]
