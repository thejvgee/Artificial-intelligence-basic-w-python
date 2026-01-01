class myQueue:
    def __init__(self):
        self._data = []

    def enqueue(self, e):
        self._data.append(e)

    def is_empty(self):
        return len(self._data) == 0

    def dequeue(self):
        if self.is_empty():
            print('дараалал хоосон байна')
            return None  # Return something to indicate the queue is empty
        print(self._data[0])
        return self._data.pop(0)  # Return the dequeued item

    def length(self):  # Changed method name to avoid conflict with the len() function
        print(len(self._data))

    def first(self):
        if not self.is_empty():
            print(self._data[0])
        else:
            print('дараалал хоосон байна')

    def printQueue(self):
        print(self._data)

# Instantiate the class and use its methods
m = myQueue()
m.enqueue(1)
m.enqueue(2)
m.printQueue()
m.length()
m.dequeue()
print(m.is_empty())
m.dequeue()
print(m.is_empty())