class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def crealist(head, i, l):
    if i > len(l):
        return
    head.next = ListNode(i)
    crealist(head.next, i + 1, l)
    return head

class Solution:
    head_reverse = None
    def reverseList(self, head):
        def dfs(head):
            if head.next is None:
                self.head_reverse = head
                return head
            nx = dfs(head.next)
            nx.next = head
            head.next = None
            return head
        if not head:
            return None
        dfs(head)
        return self.head_reverse



class Solution2:
    def reverseList(self, head):
        if not head:
            return None
        if head.next is None:
            return head
        pre = head
        head = head.next
        pre.next = None
        while True:
            if head.next is None:
                head.next = pre
                return head
            cache = head.next
            head.next = pre
            pre = head
            head = cache



head = ListNode(1)
l = [1, 2, 3, 4, 5]
head = crealist(head, 2, l)
s = Solution2()
reverhead = s.reverseList(head)

print(0)

#2
class Solution3:
    def reverseList(self, head):
        if not head or head.next is None:
            return head
        pre = head
        head = head.next
        pre.next = None
        while True:
            if head is None:
                return pre
            cache = head.next
            head.next = pre
            pre = head
            head = cache