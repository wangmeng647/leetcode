class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = pre = ListNode(-1)
        nx = 0
        while l1 and l2:
            s = l1.val + l2.val + nx
            nx = 0
            if s >= 10:
                nx = 1
                remain = s % 10
                pre.next = ListNode(remain)
            else:
                pre.next = ListNode(s)
            pre = pre.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            s = l1.val + nx
            nx = 0
            if s >= 10:
                nx = 1
                remain = s % 10
                pre.next = ListNode(remain)
            else:
                pre.next = ListNode(s)
            pre = pre.next
            l1 = l1.next
        while l2:
            s = l2.val + nx
            nx = 0
            if s >= 10:
                nx = 1
                remain = s % 10
                pre.next = ListNode(remain)
            else:
                pre.next = ListNode(s)
            pre = pre.next
            l2 = l2.next
        if nx > 0:
            pre.next = ListNode(1)
        return head.next


#2
class Solution1:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        pre = ListNode(-1)
        head = pre
        while l1 and l2:
            s = l1.val + l2.val + carry
            if s >= 10:
                head.next = ListNode(s - 10)
                carry = 1
            else:
                head.next = ListNode(s)
                carry = 0
            head = head.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            s = l1.val + carry
            if s >= 10:
                head.next = ListNode(s - 10)
                carry = 1
            else:
                head.next = ListNode(s)
                carry = 0
            l1 = l1.next
            head = head.next

        while l2:
            s = l2.val + carry
            if s >= 10:
                head.next = ListNode(s - 10)
                carry = 1
            else:
                head.next = ListNode(s)
                carry = 0
            l2 = l2.next
            head = head.next

        if carry == 0:
            return pre.next
        else:
            head.next = ListNode(1)
            return pre.next


