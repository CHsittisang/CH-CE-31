class check_point:
    def __init__(self, box1, box2, box3):
        self.statusRow1 = False
        self.statusRow2 = False
        self.statusRow3 = False
        self.jackpot = False
        self.box1 = box1
        self.box2 = box2
        self.box3 = box3
        self.point = 0

    def check_Displayslot(self):
        if self.box1[0] == self.box2[0] == self.box3[0] :
            if self.box1[0] == '🍒':
                self.point += 10
            elif self.box1[0] == '7️⃣':
                self.point += 20
            elif self.box1[0] == '💰':
                self.point += 30
            elif self.box1[0] == '💲':
                self.point += 40
            elif self.box1[0] == '🪙':
                self.point += 50
            self.statusRow1 = True
        if self.box1[1] == self.box2[1] == self.box3[1] :
            if self.box1[1] == '🍒':
                self.point += 10
            elif self.box1[1] == '7️⃣':
                self.point += 20
            elif self.box1[1] == '💰':
                self.point += 30
            elif self.box1[1] == '💲':
                self.point += 40
            elif self.box1[1] == '🪙':
                self.point += 50
            self.statusRow2 = True
        if self.box1[2] == self.box2[2] == self.box3[2] :
            if self.box1[2] == '🍒':
                self.point += 10
            elif self.box1[2] == '7️⃣':
                self.point += 20
            elif self.box1[2] == '💰':
                self.point += 30
            elif self.box1[2] == '💲':
                self.point += 40
            elif self.box1[2] == '🪙':
                self.point += 50
            self.statusRow3 = True
        if self.box1[0] == self.box2[1] == self.box3[2] :
            if self.box1[0] == '🍒':
                self.point += 10
            elif self.box1[0] == '7️⃣':
                self.point += 20
            elif self.box1[0] == '💰':
                self.point += 30
            elif self.box1[0] == '💲':
                self.point += 40
            elif self.box1[0] == '🪙':
                self.point += 50
        if self.box1[2] == self.box2[1] == self.box3[0] :
            if self.box1[2] == '🍒':
                self.point += 10
            elif self.box1[2] == '7️⃣':
                self.point += 20
            elif self.box1[2] == '💰':
                self.point += 30
            elif self.box1[2] == '💲':
                self.point += 40
            elif self.box1[2] == '🪙':
                self.point += 50
        if self.statusRow1 == True and self.statusRow2 == True and self.statusRow3 == True:
            self.jackpot = True
    def print_point(self):
        print(f'Your point is {self.point}')
 
    
    