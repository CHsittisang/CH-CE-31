class data_stack :
    def __init__(self , lst = None):
        if lst == None:
            self.items = []
        else:
            self.items = lst
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[-1]
    def push(self, i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def __str__(self):
        s = f"Stack of {self.size()} items : "
        if self.isEmpty() == False:
            for ele in self.items:
                s += str(ele) + " "
        else:
            s += "None"
        return s

# test code
thing = 'ABCDEF' 
box = data_stack()
print("\n",box.isEmpty(),"\n")
for i in thing:
    box.push(i)
    print(box)
print("\n",box.isEmpty(),"\n")
while not box.isEmpty():
    print('Pop :',box.pop(), end=' ')
    print(box)
print("\n",box.isEmpty(),"\n")