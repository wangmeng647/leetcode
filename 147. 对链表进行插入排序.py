class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def crealist(head, i, l):
    if i >= len(l):
        return
    head.next = ListNode(l[i])
    crealist(head.next, i + 1, l)

class Solution:
    def insertionSortList(self, head):
        if head.next is None:
            return head
        sentry_head = ListNode(-1)
        sentry_head.next = head
        last_ordered = head
        curr_head = head.next
        last_ordered.next = None
        while curr_head is not None:
            pre = sentry_head
            while True:
                if pre is last_ordered:
                    last_ordered.next = curr_head
                    last_ordered = curr_head
                    curr_head = curr_head.next
                    last_ordered.next = None
                    break
                if curr_head.val < pre.next.val:
                    cache_head = curr_head
                    curr_head = curr_head.next
                    cache_head.next = pre.next
                    pre.next = cache_head
                    break
                pre = pre.next
        return sentry_head.next
l = [-1,5,3,4,0]
head = ListNode(-1)
crealist(head, 1, l)
s = Solution()
r = s.insertionSortList(head)
print(0)