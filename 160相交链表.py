class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
            if headA is None or headB is None:
                return None
            index_A = headA
            index_B = headB
            while index_A is not index_B:
                if index_A is None:
                    index_A = headB
                else:
                    index_A = index_A.next
                if index_B is None:
                    index_B = headA
                else:
                    index_B = index_B.next
            return index_A


class Solution1:
    def getIntersectionNode(self, headA, headB):
        index_1 = headA
        index_2 = headB
        while True:
            if index_1 is index_2:
                return index_1
            if index_1 is None:
                index_1 = headB
            else:
                index_1 = index_1.next
            if index_2 is None:
                index_2 = headA
            else:
                index_2 = index_2.next


a = Node(2,3)
b = Node(2,3)



print(id(a))
print(id(b))



