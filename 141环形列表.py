
class Node:
    def __init__(self, x=0):
        self.x = x
        self.next = None

a = [2, 3, 4]


def creatlink(l):
    head = Node(l[0])
    tail = head
    for element in l[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head

class Solution:
    def hasCycle(self, head) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while fast != slow:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return True



head = Node()
tail = Node()
tail.next = 3
print(id(head.next))
print(id(tail.next))

#2
class Solution1:
    def hasCycle(self, head) -> bool:
        dic = set()
        while head:
            if head not in dic:
                dic.add(head)
                head = head.next
            else:
                return True
        return False

class Solution2:
    def hasCycle(self, head) -> bool:
        slow = fast = head
        if not head:
            return False
        while True:
            if fast.next is None or fast.next.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True