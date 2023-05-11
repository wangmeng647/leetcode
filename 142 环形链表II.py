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
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        slow = fast = head
        while slow.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is None or fast.next is None:
                return None
            if slow is fast:
                if slow is head:
                    return head
                while True:
                    head = head.next
                    slow = slow.next
                    if head is slow:
                        return head
        return None

class Solution2:
    def detectCycle(self, head):
        dic = set()
        while head not in dic and head is not None:
            dic.add(head)
            head = head.next
            if head in dic:
                return head
        return None
l = [1,2]
l = [3,2,0,-4]
head1 = ListNode(1)
head2 = ListNode(2)
head3 = ListNode(0)
head4 = ListNode(-1)
head1.next = head2
head2.next = head1
head3.next = head4
head4.next = head2

s = Solution()
r = s.detectCycle(head1)
print(2)
