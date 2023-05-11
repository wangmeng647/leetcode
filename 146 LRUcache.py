class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value
        self.pre = None
        self.next = None



class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.movetohead(node)
        return node.value

    def put(self, key: int, value: int):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.movetohead(node)
        node = Node(key, value)
        self.cache[key] = node
        self.addhead(node)
        self.size += 1
        if self.size > self.capacity:
            removed = self.removetail()
            self.cache.pop(removed.key)
            self.size -= 1

    def deletnode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def addhead(self, node):
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node

    def movetohead(self, node):
        self.deletnode(node)
        self.addhead(node)

    def removetail(self):
        node = self.tail.pre
        self.deletnode(node)
        return node


'''["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]'''


class LRUCache1:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.sentry = Node(-1)
        self.tail = Node(-1)
        self.sentry.next = self.tail
        self.tail.pre = self.sentry
        self.size = 0
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.movetohead(node)
        return node.value



    def put(self, key: int, value: int):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.movetohead(node)
        else:
            self.size += 1
            node = Node(key, value)
            self.cache[key] = node
            self.addhead(node)
            if self.size > self.capacity:
                key = self.tail.pre.key
                self.delethead(self.tail.pre)
                self.size -= 1
                self.cache.pop(key)


    def movetohead(self, node):
        self.delethead(node)
        self.addhead(node)

    def delethead(self, node):
        node.next.pre = node.pre
        node.pre.next = node.next

    def addhead(self, node):
        node.next = self.sentry.next
        node.next.pre = node
        node.pre = self.sentry
        self.sentry.next = node

#2
class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.sentry = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.dic = {}
        self.count = 0
        self.sentry.next = self.tail
        self.tail.pre = self.sentry
    def put(self, key, value):
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.delete_node(node)
            self.add_head(node)
        else:
            node = Node(key, value)
            self.dic[key] = node
            self.add_head(node)
            self.count += 1
            if self.count > self.capacity:
                node = self.tail.pre
                self.delete_node(node)
                self.count -= 1
                self.dic.pop(node.key)
    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self.delete_node(node)
            self.add_head(node)
            return node.val
        else:
            return -1
    def add_head(self, node):
        node.pre = self.sentry
        node.next = self.sentry.next
        self.sentry.next.pre = node
        self.sentry.next = node
    def delete_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

lru = LRUCache2(2)
lru.put(2,1)
lru.put(1,1)
lru.put(2,3)
lru.put(4,1)
r = lru.get(1)
print(r)
print(lru.get(2))
