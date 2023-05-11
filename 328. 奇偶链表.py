
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if not head:
            return None
        if head.next is None or head.next.next is None:
            return head
        head_odd = head
        head_even = head_begin_even = head.next
        while True:
            if head_even.next is None:
                break
            head_odd.next = head_even.next
            head_odd = head_odd.next
            head_even.next = head_odd.next
            head_even = head_even.next
            if not head_even:
                break
        head_odd.next = head_begin_even
        return head




#2
class Solution2:
    def oddEvenList(self, head):

        sentry_odd = head_odd = ListNode(-1)
        sentry_even = head_even = ListNode(-1)
        counts = 0
        while head:
            if counts % 2 == 0:
                head_odd.next = head
                head_odd = head_odd.next
            else:
                head_even.next = head
                head_even = head_even.next
            head = head.next
            counts += 1
        head_odd.next = sentry_even.next
        head_even.next = None
        return sentry_odd.next

l = [1,2,3,4,5]
pre = head = ListNode(-1)
for val in l:
    head.next = ListNode(val)
    head = head.next

s = Solution2()
print(s.oddEvenList(pre.next))