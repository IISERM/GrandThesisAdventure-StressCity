from tetra import gadgets
from tetra import terminal

class MyGame(terminal.Game):
    def bind_sg_events(self):
        super().bind_sg_events()
        # Other binds here

mgame = MyGame("Turing Hunt 2022", "assets/settings.json", [gadgets.Clock, gadgets.GPS, gadgets.EnergyMeter])

mgame.run()
