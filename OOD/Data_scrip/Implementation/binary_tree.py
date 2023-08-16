class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res
    def breadth_first(self, root, lv=0):
        res = []
        if root:
            res.append(f"{root.data} is in level {lv}")
            res = res + self.breadth_first(root.left, lv+1)
            res = res + self.breadth_first(root.right, lv+1)
        return res 
        

box = [15,3,16,9,23,11,7,5,34,19,2]
root = Node(15)
for i in box:
    root.insert(i)
print("Tree is :",root.printTree()) 
print("In-order is :",root.inorderTraversal(root))
print("Pre-order is :",root.preorderTraversal(root))
for j in root.breadth_first(root):
    print(j)
