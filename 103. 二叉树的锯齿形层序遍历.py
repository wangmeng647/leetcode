import copy


class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        pre_stack = []
        post_stack = []
        ans = []
        temp = []
        pre_stack.append(root)
        while pre_stack or post_stack:
            while pre_stack:
                node = pre_stack.pop()
                temp.append(node.val)
                if node.left:
                    post_stack.append(node.left)
                if node.right:
                    post_stack.append(node.right)
            if temp:
                ans.append(copy.copy(temp))
                temp.clear()
            while post_stack:
                node = post_stack.pop()
                temp.append(node.val)
                if node.right:
                    pre_stack.append(node.right)
                if node.left:
                    pre_stack.append(node.left)
            if temp:
                ans.append(copy.copy(temp))
                temp.clear()
        return ans