from creat_tree import creat_tree
class Solution:
    def invert(self, left, right):
        if left is None and right is None:
            return
        val = left.val
        left.val = right.val
        right.val = val
        self.invert(left.left, right.right)
        self.invert(left.right, right.left)


    def invertTree(self, root):
        self.invert(root, root)
        return root