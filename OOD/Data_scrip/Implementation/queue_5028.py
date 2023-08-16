class Data_Queue :
    def __init__(self, lst = None):
        if lst == None:
            self.items = []
        else:
            self.items = lst
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def enQueue(self, i):
        self.items.append(i)
    def deQueue(self):
        if self.isEmpty() == False:
            return self.items.pop(0)
        else:
            return "Queue is empty"
    def __str__(self):
        s = f"Queue of {self.size()} items : "
        if self.isEmpty() == False:
            for ele in self.items:
                s += str(ele) + " "
        else:
            s = 'Queue is empty'
        return s
12
# test code
thing = 'ABCDEF' 
box = Data_Queue()
print("\n",box.isEmpty(),"\n")
for i in thing:
    box.enQueue(i)
    print(box)
print("\n",box.isEmpty(),"\n")
while not box.isEmpty():
    print('deQueue :',box.deQueue(), "\n") 
    print(box, "\n")
print("\n",box.isEmpty(),"\n")