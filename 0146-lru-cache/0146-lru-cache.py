class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        node = self.dic[key]
        self.remove (node)
        self.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            oldNode = self.dic[key]
            self.remove(oldNode)
        
        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)

        if len(self.dic) > self.capacity:
            nodeToDelete = self.head.next
            self.remove(nodeToDelete)
            del self.dic[nodeToDelete.key]

    def add(self, node):
        previousEnd = self.tail.prev
        previousEnd.next = node
        node.prev = previousEnd
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)