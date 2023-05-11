

class Solution:
    def connect(self, root):
        if not root:
            return None
        head = ans = root
        while head.left is not None:
            curr = head
            head = head.left
            while curr.next is not None:
                curr.left.next = curr.right
                curr.right.next = curr.next.left
                curr = curr.next
            curr.left.next = curr.right
        return ans





#2
class Solution2:
    def connect(self, root):
        if not root:
            return []
        pre = root
        while root.left:
            begin = root.left
            while True:
                root.left.next = root.right
                if not root.next:
                    break
                root.right.next = root.next.left
                root = root.next
            root = begin
        return pre

