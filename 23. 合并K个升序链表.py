class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def crealist(l):
    pre = ListNode(-1)
    head = pre
    n = len(l)
    i = 0
    while i < n:
        pre.next = ListNode(l[i])
        pre = pre.next
        i += 1
    return head.next

class Solution:
    def mergeKLists(self, lists):
        n = len(lists)
        def merge(l1, l2):
            pre = ListNode(-1)
            head = pre
            while l1 and l2:
                if l1.val < l2.val:
                    pre.next = l1
                    l1 = l1.next
                else:
                    pre.next = l2
                    l2 = l2.next
                pre = pre.next
            if l1:
                pre.next = l1
            else:
                pre.next = l2
            return head.next
        def divide_merge(i, j):
            if i == j:
                return lists[i]
            if j - i == 1:
                return merge(lists[i], lists[j])
            mid = (i + j) // 2
            l1 = divide_merge(i, mid)
            l2 = divide_merge(mid + 1, j)
            return merge(l1, l2)
        if not lists:
            return None
        return divide_merge(0, n - 1)

#l = [1, 21, 11, 4, 5]
lists = [[1,4,5],[1,3,4],[2,6]]
l_head = []
for i in range(len(lists)):
    l_head.append(crealist(lists[i]))
s = Solution()
r = s.mergeKLists(l_head)
print(2)


#2
class Solution2:
    def mergeKLists(self, lists):

        def merge(l1, l2):
            head = pre = ListNode(-1)
            while l1 and l2:
                if l1.val < l2.val:
                    pre.next = l1
                    l1 = l1.next
                else:
                    pre.next = l2
                    l2 = l2.next
                pre = pre.next
            if l1:
                pre.next = l1
            if l2:
                pre.next = l2
            return head.next

        def divide(ls):
            if len(ls) == 1:
                return ls[0]
            mid = len(ls) // 2
            ls1 = divide(ls[:mid])
            ls2 = divide(ls[mid:])
            return merge(ls1, ls2)
        if not lists:
            return None
        return divide(lists)