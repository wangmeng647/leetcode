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
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        index_fast = index_slow = head
        pre_slow = ListNode(-1)
        pre_slow.next = head
        while index_fast is not None and index_fast.next is not None:
            pre_slow = pre_slow.next
            index_fast = index_fast.next.next
            index_slow = index_slow.next
        pre_slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(index_slow)
        sentry_node = ListNode(-1)
        pre = sentry_node
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        if l1 is None:
            pre.next = l2
        else:
            pre.next = l1
        return sentry_node.next


class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        if not head:
            return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummyHead = ListNode(0, head)
        subLength = 1
        while subLength < length:
            prev, curr = dummyHead, dummyHead.next
            while curr:
                head1 = curr
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break

                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None

                merged = merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
            subLength <<= 1

        return dummyHead.next






#2
class Solution3:
    def sortList(self, head):

        def merge(head):
            if not head.next:
                return head
            pre = sentry = ListNode(-1)
            pre.next = head
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                pre = pre.next
            pre.next = None
            head_1 = merge(sentry.next)
            head_2 = merge(slow)
            pre = sentry
            while head_1 and head_2:
                if head_1.val > head_2.val:
                    pre.next = head_2
                    head_2 = head_2.next
                else:
                    pre.next = head_1
                    head_1 = head_1.next
                pre = pre.next
            if head_1:
                pre.next = head_1
            else:
                pre.next = head_2
            return sentry.next
        if not head:
            return head
        return merge(head)


class Solution4:
    def sortList(self, head):
        def sort(node):
            if not node.next:
                return node
            fast = node.next
            slow = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            node2 = slow.next
            slow.next = None
            head1 = sort(node)
            head2 = sort(node2)
            sentry = pre = ListNode()
            while head1 and head2:
                if head1.val > head2.val:
                    pre.next = head2
                    head2 = head2.next
                else:
                    pre.next = head1
                    head1 = head1.next
                pre = pre.next
            if head1:
                pre.next = head1
            if head2:
                pre.next = head2
            return sentry.next
        if not head:
            return head
        return sort(head)


l = [-1,5,3,4,0]
head = ListNode(-1)
crealist(head, 1, l)

s = Solution4()
r = s.sortList(head)
print(0)
