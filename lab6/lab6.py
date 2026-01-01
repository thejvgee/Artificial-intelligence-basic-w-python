class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            print('Жагсаалт хоосон байна')
        else:
            print(self._data[-1])

    def pop(self):
        if self.is_empty():
            print("Жагсаалт хоосон байна")
        else:
            print(self._data[-1])
            self._data.pop()

    def printStack(self):
        print(self._data)

s = ArrayStack()
s.push(3)
s.push(5)
s.push(7)
s.__len__()
s.printStack()
s.top()
print(s.is_empty())
s.pop()
print(s.is_empty())

