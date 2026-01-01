class Node:
    def __init__(self, d):
        self.data = d
        self.address = None

class LinkedList:
    def __init__(self, *values):
        self.start_node = None
    
    def print_list(self):
        if self.start_node is None:
            print('Jagsaalt hooson bn!')
            return 
        else:
            n = self.start_node
            while n is not None:
                print(n.data, "")
                n = n.address
                
    def insert_front(self, data):
        new_node = Node(data)
        new_node.address = self.start_node
        self.start_node = new_node
    
    def insert_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return 
        n = self.start_node
        while n.address is not None:
            n = n.address
        n.address = new_node

    def insert_index(self, index, data):
        if index == 1:
            self.insert_front(data)
            return
        i = 1
        n = self.start_node
        while i < index - 1 and n is not None:
            n = n.address
            i = i + 1

            if n is None:
                print("index hetersen bn!")
                return
        new_node = Node(data)
        new_node.address = n.address
        n.address = new_node

    def get_count(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        while n is not None:
            count = count + 1
            n = n.address
        return count
    
    def search_item(self, x):
        if self.start_node is None:
            print('Jagsaalt hooson bn!')
            return False
        else:
            n = self.start_node
            while n is not None:
                if n.data == x:
                    print(f'{x} ur dun oldloo')
                    return True
                n = n.address
            print(f'{x} ur dun oldsngu')
            return False

    def delete_start(self):
        if self.start_node is None:
            print("jagsaalt hooson")
            return 
        self.start_node = self.start_node.address

    def delete_end(self):
        if self.start_node is None:
            print('jagsaat hooson bn!')
            return 
        n = self.start_node
        while n.address.address is not None:
            n = n.address
        n.address = None

# Code to create LinkedList instance and perform operations
l = LinkedList()
l.insert_front(11)
l.insert_front(13)
l.insert_front(15)
l.insert_front(17)
l.insert_front(18)
l.insert_front(20)
l.print_list()

l.insert_index(6, 14)
l.print_list()

l.search_item(20)
l.search_item(12)
