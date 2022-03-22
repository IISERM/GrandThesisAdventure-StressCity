from tetra import gadgets
from tetra import terminal
import CustomGadgets

class MyGame(terminal.Game):
    def bind_sg_events(self):
        super().bind_sg_events()
        self.window.bind("<KeyPress-Up>", "up")
        self.window.bind("<KeyPress-Left>", "left")
        self.window.bind("<KeyPress-Down>", "down")
        self.window.bind("<KeyPress-Right>", "right")

myGame = MyGame("Turing Hunt 2022", "assets/settings.json", "Biswas Office", [gadgets.Clock, gadgets.GPS, CustomGadgets.StressMeter, CustomGadgets.Phone])

myGame.run()
