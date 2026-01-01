class MaxHeap:
    def __init__(self):
        self.heap = []

    def get_parent(self, i):
        return (i - 1) // 2
    
    def get_leftChild(self, i):
        return 2 * i + 1

    def get_rightChild(self, i):
        return 2 * i + 2

    def has_parent(self, i):
        return self.get_parent(i) >= 0
    
    def has_rightChild(self, i):
        return self.get_leftChild(i) < len(self.heap)
    
    def has_leftChild(self, i):
        return self.get_rightChild(i) < len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def print_heap(self):
        print(self.heap)

    def insert(self, key):
        self.heap.append(key)
        self.heap_up(len(self.heap) - 1)

    def heap_up(self, i):
        while self.has_parent(i) and self.heap[i] > self.heap[self.get_parent(i)]:
            self.swap(i, self.get_parent(i))
            i = self.get_parent(i)

# Create an instance of MaxHeap
mx = MaxHeap()

mx.insert(99)
mx.insert(45)
mx.insert(63)
mx.insert(35)
mx.insert(29)
mx.insert(57)
mx.insert(42)
mx.insert(27)
mx.insert(12)
mx.insert(24)

mx.print_heap()

mx.insert(11)
mx.print_heap()