class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def creat_tree(root , lis):
    if len(lis) == 0:
        return root
    if lis[0] is not None:
        root = TreeNode(lis[0])
        lis.pop(0)
        root.left = creat_tree(root.left, lis)
        root.right = creat_tree(root.right, lis)
        return root
    else:
        root = None
        lis.pop(0)
        return root

lis = [1,None,2,3]
tree_root = creat_tree(None, lis)
traversal_lis = []
class Solution_recursion:
    def inorderTraversal(self, root):
        if root is None:
            return
        self.inorderTraversal(root.left)
        val = root.val
        traversal_lis.append(val)
        self.inorderTraversal(root.right)
        return traversal_lis

class Solution_iteration:
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

class Solution_morris:
    def inorderTraversal(self, root):
        res = []
        while root:
            if root.left:
                # find out predecessor
                predecessor = root.left
                while predecessor.right:
                    predecessor = predecessor.right
                # link predecessor to root
                predecessor.right = root
                # set left child of root to None
                temp = root
                root = root.left
                temp.left = None
            else:
                res.append(root.val)
                root = root.right
        return res

s = Solution_morris()
print(s.inorderTraversal(tree_root))

class Solution_recursion1:
    def inorderTraversal(self, root):
        ans = []
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            ans.append(node.val)
            traverse(node.right)
        traverse(root)
        return ans
