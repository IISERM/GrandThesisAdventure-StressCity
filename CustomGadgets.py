from tetra import gadgets
import PySimpleGUI as sg
import random
from tetra import helpers

class StressMeter(gadgets.Gadget):
    def __init__(self, game):
        super().__init__("Stress Meter")
        self.val = 25
        self.stress_rate_per_iteration = 0.001
        self.isBroken = False

    def stress_saying(self):
        return random.choice([
            'I\'m way too stressed to do anything',
            "Even Aulak's classes were less stressful than this.",
            "Holy F***. I'd take offline exams instead of this any day!",
            "And here I thought Phi@I's treasure hunts were the most exhausting.",
            "Should have just opted for online labs man.",
            "Should have just gone to Physictionary.\nIt would have been boring, but atleast it wouldn't be so stressful...",
            "Sir, I think you are muted. Oh wait, I'm not in class.",
            "F... this is longer than Kuljit's class..."
        ])

    def render_content(self):
        return sg.ProgressBar(100, orientation='h', size=(30, 10), key=self.name.lower(), expand_x=True, pad=10)

    def update(self, game, event):
        self.val += self.stress_rate_per_iteration
        if self.val > 100 and not self.isBroken:
            self.isBroken = True
            sg.popup_no_buttons("Stress levels have surpassed 100%. Your Stress Meter broke down.",
                                auto_close=True, auto_close_duration=3, no_titlebar=True, modal=True)
        elif self.val > 100 and self.isBroken and self.val%500 == 0:
            sg.popup_no_buttons(self.stress_saying(), auto_close = True, auto_close_duration = 2, no_titlebar = True, modal = True)
        else:
            game.window[self.name.lower()].UpdateBar(self.val)

class Phone(gadgets.Gadget):
    def __init__(self, game):
        super().__init__("Phone")
        self.notificationsActive = False
        self.messageFromFriend = True

    def render_content(self):
        return sg.Button("Phone", key = "OPEN-PHONE")
        
    def update(self, game, event):
        count = 0
        if event == "OPEN-PHONE":
            if not self.messageFromFriend:
                sg.popup_no_buttons("This should display an image", auto_close = True, auto_close_duration = 2, no_titlebar = True, modal = True)
            else:
                pass
            
        if self.notificationsActive and random.random()<0.6 :
            sg.popup_no_buttons("I should check my phone, if there's a message from the PhD guy...", auto_close = True, auto_close_duration = 2, no_titlebar = True, modal = True)
            count += 1
        if self.notificationsActive and count == 10:
            sg.popup_no_buttons("There's something on my phone", auto_close = True, auto_close_duration = 2, no_titlebar = True, modal = True)
            game.map("CAF").place_item("X Marks The Spot!", game)