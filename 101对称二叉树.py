from creat_tree import creat_tree


class Solution:
    def check(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.val == right.val and self.check(left.left, right.right) and self.check(left.right, right.left)
    def isSymmetric(self, root):
        return self.check(root, root)


lis = [1, 2, 3,None,None,4,None,None,2,4,None,None,3,None,None]
tree_root = creat_tree(None, lis)
s = Solution()
print(s.isSymmetric(tree_root))