
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''class Solution:
    def buildTree(self, preorder, inorder):
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None

            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]

            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left,
                                    inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1,
                                     inorder_right)
            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)'''


class Solution:
    def buildTree(self, preorder, inorder):
        def mybuildtree(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            root = preorder[preorder_left]
            index_inorder = index[root]
            root = TreeNode(root)
            left_leave_size = index_inorder - inorder_left
            root.left = mybuildtree(preorder_left + 1, preorder_left + left_leave_size, inorder_left, index_inorder - 1)
            root.right = mybuildtree(preorder_left + left_leave_size + 1, preorder_right, index_inorder + 1,
                                     inorder_right)
            return root
        index = {element: i for i, element in enumerate(inorder)}
        n = len(preorder)
        return mybuildtree(0, n - 1, 0, n - 1)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
s = Solution()
mytree = s.buildTree(preorder, inorder)
print(2)


#2
class Solution2:
    def buildTree(self, preorder, inorder):

        def tree_build(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r:
                return None

            root = TreeNode(preorder[pre_l])
            index = dic[preorder[pre_l]]
            left_size = index - in_l
            root.left = tree_build(pre_l + 1, pre_l + left_size, in_l, index - 1)
            root.right = tree_build(pre_l + left_size + 1, pre_r, index + 1, in_r)
            return root

        dic = {element: i for i, element in enumerate(inorder)}
        n = len(preorder)
        return tree_build(0, n - 1, 0, n - 1)




