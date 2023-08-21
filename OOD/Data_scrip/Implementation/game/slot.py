import random

class slot_Data :
    def __init__(self):
        self.item = ['a','b','c','d','e','f','g','h','i']
        self.box1 = []
        self.box2 = []
        self.box3 = []
        self.point = 0
        self.per_win = 0
    def isEmpty(self):
        return self.box1 == [] and self.box2 == [] and self.box3 == []
    def size(self):
        return len(self.box1) + len(self.box2) + len(self.box3)
    def enQueue(self):
        if self.per_win < 5:
            while self.size() < 9:
                self.box1.append(random.choice(self.item))
                self.box2.append(random.choice(self.item))
                self.box3.append(random.choice(self.item))
            self.per_win += 1
        elif self.per_win >= 5 and self.per_win < 10:
            while self.size() < 6:
                self.box1.append(random.choice(self.item))
                self.box2.append(random.choice(self.item))
                self.box3.append(random.choice(self.item))
            self.per_win += 1
        elif self.per_win >= 10 and self.per_win < 15:
            while self.size() < 6:
                self.box1.append(random.choice(self.item))
                self.box2.append(random.choice(self.item))
                self.box3.append(random.choice(self.item))
            self.per_win += 1
    def deQueue(self):
        if self.isEmpty() == False:
            return self.box1.pop(0), self.box2.pop(0), self.box3.pop(0)
        else:
            return "Queue is empty"
    def check_Displayslot(self):
        if self.box1[0] == self.box1[1] == self.box1[2] :
            self.point += 1
        if self.box2[0] == self.box2[1] == self.box2[2] :
            self.point += 1
        if self.box3[0] == self.box3[1] == self.box3[2] :
            self.point += 1
        if self.box1[0] == self.box2[1] == self.box3[2] :
            self.point += 1
        if self.box1[2] == self.box2[1] == self.box3[0] :
            self.point += 1
    def total_point(self):
        if self.point == 1:
            return 10
        elif self.point == 2:
            return 20
        elif self.point == 3:
            return 30
        elif self.point == 4:
            return 40
        elif self.point == 5:
            return 100
        else:
            return 0
    def __str__(self):  
        s = f"Queue of {self.size()} items \n"
        if self.isEmpty() == False:
            for ele in self.box1:
                s += str(ele) + " "
            s += "\n"
            for ele in self.box2:
                s += str(ele) + " "
            s += "\n"
            for ele in self.box3:
                s += str(ele) + " "
        else:
            s = 'Queue is empty'
        return s

# test code
box = slot_Data()
print("\n",box.isEmpty(),"\n")
box.enQueue()
box.check_Displayslot()
print(box.total_point(),"\n")
print('\n',"*"*20,'\n')
print(box.box1)
print(box.box2)
print(box.box3)