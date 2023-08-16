# from queue import Queue

# def shuffle(string1,string2):
#     q1 = Queue(maxsize=50)
#     for s in string1:
#         q1.put(s)
        
#     q2 = Queue(maxsize=50)
#     for s in string2:
#         q2.put(s)

#     ret = ""
#     while not q1.empty() or not q2.empty:
#         if not q1.empty() :
#             ret += q1.get()
#         if not q2.empty() :
#             ret += q2.get()
#     return ret

# st1 = "abcdefg"
# st2 = "ABC" 
# print(shuffle(st1,st2)) #aAbBcCdDeEfFgG

#
# สร้างฟังก์ชั่น insert_sorted() สำหรับ insert ข้อมูลใน linked list แบบเรียงลำดับข้อมูลจากน้อยไปหามาก
#

class Node:
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode

  def insert_sorted(self,data):
    newNode = Node(data)
    inserted = False
    if(self.head):
      current = self.head      
      if current.data >= data:
        newNode.next = current
        self.head = newNode
        inserted = True
      else:  
        while(current.next and not inserted ):
          nextnode = current.next
          if current.data <= data and data <= nextnode.data:
            newNode.next = nextnode
            current.next = newNode
            inserted = True
          current = current.next
      
      if not inserted:
        current.next = newNode
    else:
      self.head = newNode

  # print method for the linked list
  def printLL(self):
    ret = []
    current = self.head
    while(current):
      print(current.data,end=" ")
      ret += [str(current.data)]
      current = current.next
    print(end="\n")
    return ' '.join(ret)
    

# Singly Linked List with insertion and print methods
print("Normal Linked List")
LL = LinkedList()
LL.insert(3)
LL.insert(40)
LL.insert(5)
LL.insert(10)
LL.insert(8)
LL.printLL()

# Singly Linked List with sorted insertion and print methods
print("Sorted Linked List")
LL = LinkedList()
LL.insert_sorted(3)
LL.insert_sorted(40)
LL.insert_sorted(5)
LL.insert_sorted(10)
LL.insert_sorted(8)
LL.printLL()
