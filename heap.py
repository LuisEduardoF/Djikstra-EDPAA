class Heap():
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i][0] < self.heap[parent][0]:
            self.swap(i, parent)
            self._heapify_up(parent)
    
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val
    
    def _heapify_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)
         
        if left < len(self.heap) and self.heap[left][0] < self.heap[min_index][0]:
            min_index = left
        
        if right < len(self.heap) and self.heap[right][0] < self.heap[min_index][0]:
            min_index = right
        
        if min_index != i:
            self.swap(i, min_index)
            self._heapify_down(min_index)
    
    def get_min(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def __str__(self):
        return str(self.heap)