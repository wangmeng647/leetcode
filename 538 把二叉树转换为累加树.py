

class Solution:
    def __init__(self):
        self.s = 0
    def convertBST(self, root):
        def traverse(root):
            if root is None:
                return
            traverse(root.right)
            self.s += root.val
            root.val = self.s
            traverse(root.left)
        traverse(root)
        return root