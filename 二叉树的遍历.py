from creat_tree import creat_tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#递归
'''class Solution_inorder:
    def inorderTraversal(self, root):
        lis = []
        self.inorder(root, lis)
        return lis


    def inorder(self, root, lis):
        if root is None:
            return
        r = root
        self.inorderTraversal(r.left, lis)
        lis.append(r.val)
        self.inorderTraversal(r.right, lis)'''

#迭代
class Solution_inorder:
    def inorderTraversal(self, root):
        stack = []
        traversal_lis = []
        while stack or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            traversal_lis.append(root.val)
            root = root.right
        return traversal_lis

#递归
class Solution_postorder:
    def postorderTraversal(self, root):
        lis = []
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            dfs(root.right)
            lis.append(root.val)
        dfs(root)
        return lis




l= [1,2,None,None,3]
root = creat_tree(None, l)
s = Solution_postorder()
print(s.postorderTraversal(root))