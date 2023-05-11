

class Solution:
    def removeNthFromEnd(self, head, n: int):
        index = head
        counts = 0
        if head.next is None:
            return None
        while index.next is not None:
            index = index.next
            counts += 1
        differ = counts - n
        if differ < 0:
            cache_head = head
            head = head.next
            cache_head.next = None
            return head
        cache_head = head
        while differ > 0:
            cache_head = cache_head.next
            differ -= 1
        if n == 1:
            cache_head.next = None
            return head
        else:
            head2 = cache_head.next
            cache_head.next = cache_head.next.next
            head2.next = None
            return head




#2
class Solution1:
    def removeNthFromEnd(self, head, n: int):
        count = 0
        fast = slow = head
        while count < n:
            fast = fast.next
            count += 1
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
