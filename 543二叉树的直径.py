from creat_tree import creat_tree

class Solution:
    def __init__(self):
        self.ans = 0
    def maxdepth(self, root):
        if root is None:
            return 0
        l = self.maxdepth(root.left)
        r = self.maxdepth(root.right)
        self.ans = max(self.ans, l + r)
        return max(l, r) + 1
    def diameterOfBinaryTree(self, root):
        self.maxdepth(root)
        return self.ans

