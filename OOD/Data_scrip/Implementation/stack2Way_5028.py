class Data_stack2Way:
    def __init__(self, lst = None):
        if lst == None:
            self.items = []
        else:
            self.items = lst
            
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def right_peek(self):
        return self.items[-1]
    def left_peek(self):
        return self.items[0]
    def right_push(self, i):
        self.items.append(i)
    def left_push(self, i):
        self.items.insert(0, i)
    def right_pop(self):
        return self.items.pop()
    def left_pop(self):
        return self.items.pop(0)
    def __str__(self):
        s = f"Stack of {self.size()} items : "
        if self.isEmpty() == False:
            for ele in self.items:
                s += str(ele) + " "
        else:
            s += "None"
        return s
    
# test code
def inleft_outleft(x,y):
    print(f'\nPush {y} to left stack\n')
    for i in y:
        box.left_push(i)
        print(x)
    print(f'\nPop left stack\n')
    while not x.isEmpty():
        print('Pop :',x.left_pop(), end=' ')
        print(x)
def inright_outright(x,y):
    print(f'\nPush {y} to right stack\n')
    for i in y:
        box.right_push(i)
        print(x)
    print(f'\nPop right stack\n')
    while not x.isEmpty():
        print('Pop :',x.right_pop(), end=' ')
        print(x)
def inleft_outright(x,y):
    print(f'\nPush {y} to left stack\n')
    for i in y:
        box.left_push(i)
        print(x)
    print(f'\nPop right stack\n')
    while not x.isEmpty():
        print('Pop :',x.right_pop(), end=' ')
        print(x)
def inright_outleft(x,y):
    print(f'\nPush {y} to right stack\n')
    for i in y:
        box.right_push(i)
        print(x)
    print(f'\nPop left stack\n')
    while not x.isEmpty():
        print('Pop :',x.left_pop(), end=' ')
        print(x)

thing = 'ABCD'
box = Data_stack2Way()
inleft_outleft(box,thing)
print('\n-----------------------------------')
inright_outright(box,thing)
print('\n-----------------------------------')
inleft_outright(box,thing)
print('\n-----------------------------------')
inright_outleft(box,thing)
print('\n-----------------------------------')