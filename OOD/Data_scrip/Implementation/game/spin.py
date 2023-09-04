import random

class spin:
    def __init__(self, win_rate):
        self.item = ['🍒','7️⃣','💰','💲','🪙']
        self.box1 = []
        self.box2 = []
        self.box3 = []
        self.jackpot = False
        self.win_rate = win_rate