class node :
    def __init__(self, data, next = None):
        self.data =data
        if next is None:
            self.next = None 
        else:
            self.next = next
    
class link_List:
    def __init__(self):
        self.head = None
    def append(self,data):
        p = node(data)
        if self.head == None :
            self.head = p 
        else :
            t = self.head 
            while t.next != None :
                t = t.next 
            t.next = p

    def insert(self, index, data):
        p = node(data)
        if index == 0 :
            p.next = self.head
            self.head = p
        else : 
            t = self.head
            for i in range(index-1):
                t = t.next
            p.next = t.next
            t.next = p
    def delete(self, index):
        if index == 0 :
            self.head = self.head.next
        else :
            t = self.head
            for i in range(index-1):
                t = t.next
            t.next = t.next.next
    def search(self, data):
        t = self.head
        while t != None:
            if t.data == data:
                return True
            t = t.next
        return False
    def __str__(self):
        s = ''
        t = self.head
        while t != None:
            s += str(t.data) + ' '
            t = t.next
        return s

# test code 
thing = 'ABCDEF'
box = link_List()
for i in thing:
    box.append(i)
    print(box)
for i in "XYZ":
    box.insert(3,i)
print(box)
            