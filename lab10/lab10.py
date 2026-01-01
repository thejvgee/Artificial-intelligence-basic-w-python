class Tree():
    def __init__(self,root):
        self._root = root
        self.children = []

    def addNode(self,obj):
        self.children.append(obj)

class Node():
    def __init__(self,data):
        self._data = data
        self.children = []
    
    def addNode(self,obj):
        self.children.append(obj)
    
altan_urag = Tree('Есүхэй')
altan_urag.addNode('Хасар')
altan_urag.addNode('Тэмүүжин')