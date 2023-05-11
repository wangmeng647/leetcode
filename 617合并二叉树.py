from creat_tree import creat_tree

class Solution:
    def mergeTrees(self, root1, root2):
        def traverse(root1, root2):
            if not root1:
                #root1 = root2
                return root2
            if not root2:
                return root1
            root1.val = root1.val + root2.val
            root1.left = traverse(root1.left, root2.left)
            root1.right = traverse(root1.right, root2.right)
            return root1
        return traverse(root1, root2)
lis1 = [1,3,5,None,None,None,2]
lis2 = [2,1,None,4,None,None,3,None,7,None,None]
root1 = creat_tree(None, lis1)
root2 = creat_tree(None,lis2)
s = Solution()
root = s.mergeTrees(root1, root2)