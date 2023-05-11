import copy
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        head_copy = copy.deepcopy(head)
        return head_copy

'''a = Node(2)
b = Node(3)
a.next = b
c = copy.deepcopy(a)'''
a = [[1,2,[5,[0,6]]],3]
b = copy.deepcopy(a)
c = copy.copy(a)
print(id(a[0][1]))
print(id(c[0][1]))
print(id(b[0][1]))
a[0] = 4
print(a)
print(b)
print(c)
