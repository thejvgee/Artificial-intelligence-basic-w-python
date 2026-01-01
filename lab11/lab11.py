class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def insert(self,data):
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
            print(self.data),
        if self.right:
            self.right.printTree()
    
    def findval(self,s_value):
        if s_value<self.data:
            if self.left is None:
                print(f"'{s_value}'-r ur dun oldsngu!")
                return
            return self.left.findval(s_value)
        elif s_value > self.data:
            if self.right is None:
                print(f"'{s_value}'-r ur dun oldsngu!")
                return
            return self.right.findval(s_value)
        else:
            return print(f"'{str(self.data)}'-r ur dun oldloo!")


bst = Node(11)
bst.insert(23)
bst.insert(43)
bst.insert(43)
bst.insert(53)
bst.insert(85)
bst.insert(68)
bst.insert(19)

bst.printTree()
bst.findval(23)
bst.findval(85)
