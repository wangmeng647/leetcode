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
    def mergeTwoLists(self, list1, list2):
        pre_head = ListNode(-1)
        pre = pre_head
        while list1 and list2:
            if list1.val < list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2
                list2 = list2.next
            pre = pre.next
        pre.next = list1 if list1 is not None else list2
        return pre_head.next


class Solution1:
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2














class Solution2:
    def mergeTwoLists(self, list1, list2):
        pre_head = ListNode(-1)
        pre = pre_head
        while list1 and list2:
            if list1.val < list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2
                list2 = list2.next
            pre = pre.next
        pre.next = list1 if list1 is not None else list2
        return pre_head.next



head1 = ListNode(1)
l1 = [1,2,4]
head1 = crealist(head1, 2, l1)
head2 = ListNode(1)
l2 = [1,3,4]
head2 = crealist(head2, 2, l1)
s = Solution1()
print(s.mergeTwoLists(head1, head2))