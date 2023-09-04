class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None 
        self.next = None

class DCList: # notation as Doubly Circular Linked List
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, item: Node):
        if not isinstance(item, Node):
            item = Node(item)     

        if self.head is None:
            self.head = item
            self.tail = item
            self.head.next = self.tail 
            self.head.prev = self.tail
            self.tail.next = self.head
            self.tail.prev = self.head
        else:
            item.prev = self.tail
            item.next = self.head
            self.tail.next = item
            self.head.prev = item
            self.tail = item
        self.length += 1

    def pop(self, index: int = -1):
        if self.head is None or self.length == 0:
            raise IndexError("pop from empty DClist")

        if index < 0:
            index += self.length

        if index == 0:
            data = self.head.data
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = self.tail
            else:
                self.tail = None

        elif index == self.length - 1:
            data = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = self.head
        elif 0 < index < self.length:
            current = self.head
            for _ in range(index):
                current = current.next
            prev_node = current.prev
            next_node = current.next
            prev_node.next = next_node
            next_node.prev = prev_node
            data = current.data
        else:
            raise IndexError("DCList index out of range")

        self.length -= 1
        return data

    def sort(self):
        if self.head is None:
            return

        sorted_nodes = sorted(self, key=lambda node: str(node.data))

        self.head = sorted_nodes[0]
        current = self.head
        for next_node in sorted_nodes[1:]:
            current.next = next_node
            next_node.prev = current
            current = next_node
        self.tail = current
        self.tail.next = self.head
        self.head.prev = self.tail

    def is_empty(self):
        return True if self.length == 0 else False

    def find(self, value):
        if self.head is None or self.length == 0:
            return None
    
        current = self.head
        index = 0
        while current != self.tail:
            if current.data == value:
                return index
            current = current.next
            index += 1
        if self.tail.data == value:
            return index
        return ""

    def insert(self, index, item):
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds for insertion")

        new_node = Node(item)

        if index == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node.prev = new_node
            else:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.head = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node
        else:
            current = self.head 
            for _ in range(index):
                current = current.next
            prev_node = current.prev
            new_node.prev = prev_node
            new_node.next = current
            prev_node.next = new_node
            current.prev = new_node

        self.length += 1

    def __iter__(self):
        current = self.head
        while current is not None and current != self.tail:
            yield current
            current = current.next
        if current is not None:
            yield current
            
    def __len__(self):
        return self.length
    
    def __str__(self):
        if self.head is None:
            return "[]"

        elements = []
        current = self.head
        while current != self.tail:
            elements.append(repr(current.data)) 
            current = current.next
        elements.append(repr(self.tail.data))

        return "[" + ", ".join(elements) + "]"
    
    def __getitem__(self, index):
        if index < 0 :
            index += self.length

        if index < 0 or index >= self.length:
            raise IndexError("Out of range")

        sub_lst = self.head
        for i in range(index):
            sub_lst = sub_lst.next
        
        return sub_lst.data





thing = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
box = DCList()
for i in thing:
    box.append(i)
    print(box)
print(box[2])
box.sort()
print(box)
print(box[2])



# dclst = [i for i in range(100)]
# dclst.sort()
# print(dclst) 
# print(f"\nfound at: ", dclst.find(9))
# dclst.insert(999, 3)
# print(len(dclst))
# tdclend = time.time()
# print(f"list time:", tlend - tlst, "sec")
# print(f"DCList time:", tdclend - tlend, "sec")