class DEQueue:
    def __init__(self):
        self._data = []

    def add_first(self, e):
        self._data.insert(0,e)
    def add_last(self,e):
        self._data.append(e)

    def delete_first(self):
        self._data.pop(0)
    
    def delete_last(self):
        self._data.pop()

    def first(self):
        print(self._data[0])
    
    def last(self):
        print(self._data[-1])

    def is_empty(self):
        return len(self._data) == 0

    def len(self):
        print(len(self._data))
    def printDEQueue(self):
            print(self._data)
        
    
deq = DEQueue()
deq.add_first(1)
deq.add_first(12)
deq.add_first(11)
deq.add_first(13)
deq.add_first(14)
deq.add_first(115)
deq.add_first(112)
deq.printDEQueue()
deq.first()
deq.delete_last()
deq.delete_first()
deq.add_last(21)
deq.add_last(22)
deq.add_last(22)
deq.printDEQueue()

print(deq.is_empty())