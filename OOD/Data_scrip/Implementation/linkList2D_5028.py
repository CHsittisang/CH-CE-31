class pimaryNode:
    def __init__(self, pimary_data):
        self.pimaryData = pimary_data
        self.secondaryNext = None
        self.pimaryNext = None
class secondaryNode:
    def __init__(self, secondary_data):
        self.secondaryData = secondary_data
        self.secondaryNext = None
class Link_list2D:
    def __init__(self):
        self.head = None
    def append_pimary(self, pimary_data):
        p = pimaryNode(pimary_data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.pimaryNext != None:
                t = t.pimaryNext
            t.pimaryNext = p
    def append_secondary(self, pimary_data, secondary_data):
        t = secondaryNode(secondary_data)
        p = self.head
        while p != None:
            if p.pimaryData == pimary_data:
                if p.secondaryNext == None:
                    p.secondaryNext = t
                else:
                    s = p.secondaryNext
                    while s.secondaryNext != None:
                        s = s.secondaryNext
                    s.secondaryNext = t
                return 
            p = p.pimaryNext
        print('pimary data not found')

    def insert_pimary(self, pimary_index, pimary_data):
        p = pimaryNode(pimary_data)
        if pimary_index == 0:
            p.pimaryNext = self.head
            self.head = p
        else:
            t = self.head
            for i in range(pimary_index-1):
                t = t.pimaryNext
            p.pimaryNext = t.pimaryNext
            t.pimaryNext = p
    def insert_secondary(self, pimary_data, secondary_index, secondary_data):
        t = secondaryNode(secondary_data)
        p = self.head
        while p != None:
            if p.pimaryData == pimary_data:
                if secondary_index == 0:
                    t.secondaryNext = p.secondaryNext
                    p.secondaryNext = t
                else:
                    s = p.secondaryNext
                    for i in range(secondary_index-1):
                        s = s.secondaryNext
                    t.secondaryNext = s.secondaryNext
                    s.secondaryNext = t
                return
            p = p.pimaryNext
        print('pimary data not found')
    def delete_pimary(self, pimary_index):
        if pimary_index == 0:
            self.head = self.head.pimaryNext
        else:
            t = self.head
            for i in range(pimary_index-1):
                t = t.pimaryNext
            t.pimaryNext = t.pimaryNext.pimaryNext
    def delete_secondary(self, pimary_data, secondary_index):
        p = self.head
        while p != None:
            if p.pimaryData == pimary_data:
                if secondary_index == 0:
                    p.secondaryNext = p.secondaryNext.secondaryNext
                else:
                    s = p.secondaryNext
                    for i in range(secondary_index-1):
                        s = s.secondaryNext
                    s.secondaryNext = s.secondaryNext.secondaryNext
                return
            p = p.pimaryNext
        print('pimary data not found')
    def search_pimary(self, pimary_data):
        p = self.head
        while p != None:
            if p.pimaryData == pimary_data:
                return True
            p = p.pimaryNext
        return False
    def search_secondary(self, pimary_data, secondary_data):
        p = self.head
        while p != None:
            if p.pimaryData == pimary_data:
                s = p.secondaryNext
                while s != None:
                    if s.secondaryData == secondary_data:
                        return True
                    s = s.secondaryNext
                return False
            p = p.pimaryNext
        return False
    def __str__(self):
        s = ''
        p = self.head  
        while p != None:
            s += str(p.pimaryData) + ':'
            s += '{'
            while p.secondaryNext != None:
                s += str(p.secondaryNext.secondaryData)
                p.secondaryNext = p.secondaryNext.secondaryNext
            s += '}'
            s += '->'
            p = p.pimaryNext
        s += 'None'
        return s
    
# test code
box = Link_list2D()
print(box)
box.append_pimary('A')
box.append_pimary('B')
box.append_pimary('C')
box.append_secondary('A', 'a')
box.append_secondary('A', 'b')
box.append_secondary('A', 'c')
box.append_secondary('B', 'd')
box.append_secondary('B', 'e')
box.append_secondary('B', 'f')
box.append_secondary('C', 'g')
box.append_secondary('C', 'h')
box.append_secondary('C', 'i')
box.insert_pimary(0, 'D')
box.insert_pimary(1, 'E')
box.insert_pimary(2, 'F')
box.insert_secondary('D', 0, 'j')
box.insert_secondary('D', 1, 'k')
box.insert_secondary('D', 2, 'l')
box.insert_secondary('E', 0, 'm')
box.insert_secondary('E', 1, 'n')
box.insert_secondary('E', 2, 'o')
box.insert_secondary('F', 0, 'p')
box.insert_secondary('F', 1, 'q')
box.insert_secondary('F', 2, 'r')
print(box)
#test git
            
