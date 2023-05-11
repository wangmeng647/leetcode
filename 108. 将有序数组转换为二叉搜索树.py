class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        r = len(nums) - 1
        def create_tree(l, r):
            if r < l:
                return None
            if l == r:
                return TreeNode(nums[l])
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = create_tree(l, mid - 1)
            root.right = create_tree(mid + 1, r)
            return root
        return create_tree(0, r)

print(0)















class Solution1:
    def sortedArrayToBST(self, nums):
        n = len(nums)
        r = n - 1
        l = 0
        def create_tree(l, r):
            if l == r:
                return TreeNode(nums[l])
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = create_tree(l, mid - 1)
            root.right = create_tree(mid + 1, r)
            return root
        return create_tree(l, r)