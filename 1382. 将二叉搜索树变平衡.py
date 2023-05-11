class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.father = None
        self.height = 0

from AVL import AVL


class Solution:
    def balanceBST(self, root):
        cache = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            cache.append(node.val)
            traverse(node.right)
        traverse(root)
        avl = AVL()
        for n in cache:
            avl.insert(n)
        return avl.root