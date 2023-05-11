

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        node.next.next = None





#2
class Solution2:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next