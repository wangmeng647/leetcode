

class Solution:
    def rotateRight(self, head, k: int):
        n = 1
        head_last = pre = head
        if not head:
            return head
        while head_last.next:
            head_last = head_last.next
            n += 1
        head_last.next = head
        k = k % n
        steps = n - k
        for _ in range(steps - 1):
            pre = pre.next
        new_head = pre.next
        pre.next = None
        return new_head