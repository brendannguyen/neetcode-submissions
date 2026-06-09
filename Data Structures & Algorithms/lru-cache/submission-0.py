class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}

        # left <-> nodeA <-> nodeB <-> nodeC <-> right
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.data:
            self.remove(self.data[key])
            self.insert(self.data[key])
            return self.data[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.remove(self.data[key])
        
        self.data[key] = Node(key, value)
        self.insert(self.data[key])
        
        if len(self.data) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            self.data.pop(lru.key)
       




