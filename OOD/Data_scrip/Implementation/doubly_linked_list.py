# doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self, lst = None):
        if lst == None:
            self.head = None
            self.tail = None
        else:
            self.head = Node(lst[0])
            self.tail = self.head
            for i in range(1,len(lst)):
                self.tail.next = Node(lst[i])
                self.tail.next.prev = self.tail
                self.tail = self.tail.next
    def __str__(self):
        s = "List : "
        p = self.head
        while p != None:
            s += str(p.data) + " "
            p = p.next
        return s
    def __len__(self):
        p = self.head
        count = 0
        while p != None:
            count += 1
            p = p.next
        return count
    def isEmpty(self):
        return self.head == None
    def append(self, item):
        if self.isEmpty():
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
    def addHead(self, item):
        if self.isEmpty():
            self.head = Node(item)
            self.tail = self.head
        else:
            self.head.prev = Node(item)
            self.head.prev.next = self.head
            self.head = self.head.prev
    def insert(self, pos, item):
        if pos <= 0:
            self.addHead(item)
        elif pos >= len(self):
            self.append(item)
        else:
            p = self.head
            while pos > 1:
                p = p.next
                pos -= 1
            q = Node(item)
            q.next = p.next
            q.prev = p
            p.next.prev = q
            p.next = q
    def search(self, item):
        p = self.head
        while p != None:
            if p.data == item:
                return "Found"
            p = p.next
        return "Not Found"
    def index(self, item):
        p = self.head
        count = 0
        while p != None:
            if p.data == item:
                return count
            count += 1
            p = p.next
        return "Not Found"
    def pop(self, pos):
        if pos <= 0:
            self.head = self.head.next
            self.head.prev = None
        elif pos >= len(self)-1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:  
            p = self.head
            while pos > 0:
                p = p.next
                pos -= 1
            p.prev.next = p.next
            p.next.prev = p.prev
    def remove(self, item):
        if self.search(item) == "Found":
            self.pop(self.index(item))
        else:
            return "Not Found"
    def size(self):
        return len(self)

# test code
box = DoublyLinkedList()
print(box.isEmpty())
box.append(1)
box.append(2)
box.append(3)
box.append(4)
box.append(5)
box.addHead(0)
box.addHead(-1)
box.addHead(-2)
box.insert(3, 99)
print(box)
print(box.search(99))
print(box.index(99))
box.pop(3)
print(box)  
box.remove(99)
print(box)
print(box.size())
print(box.isEmpty())
print(box.tail.data)
print(box.head.data)
print(box.tail.prev.data)
print(box.head.next.data)
print(box.tail.prev.prev.data)
print(box.head.next.next.data)

