# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def creat_tree(lis):
    if not lis:
        return None
    head = node = TreeNode(lis.pop(0))
    que = []
    que.append(node)
    while lis:
        node = que.pop(0)
        if lis[0] is not None:
            node.left = TreeNode(lis.pop(0))
            que.append(node.left)
        else:
            lis.pop(0)
        if lis[0] is not None:
            node.right = TreeNode(lis.pop(0))
            que.append(node.right)
        else:
            lis.pop(0)
    return head



class Solution:
    def kthSmallest(self, root, k: int) -> int:
        ans = 0
        counts = 0
        r = False
        def traverse(node):
            nonlocal counts, r, ans
            if r:
                return
            if node is None:
                return
            traverse(node.left)
            if r:
                return
            counts += 1
            if counts == k:
                r = True
                ans = node.val
                return
            traverse(node.right)
        traverse(root)
        return ans



l = [5,3,6,2,4,None,None,1, None]
root = creat_tree(l)
s = Solution()
print(s.kthSmallest(root, 2))