import collections

from creat_tree import creat_tree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    lis = ''
    def serialize(self, root):
        def traverse(root):
            if root is None:
                self.lis += 'None' + ','
                return
            self.lis += str(root.val) + ','
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        self.lis = self.lis[:-1]
        return self.lis

    def deserialize(self, data):
        def creat_t(root, data):
            if len(data) == 0:
                return root
            if data[0] != 'None':
                root = TreeNode(int(data[0]))
                data.popleft()
                root.left = creat_t(root.left, data)
                root.right = creat_t(root.right, data)
                return root
            else:
                data.popleft()
                return root
        data = data.split(',')
        data = collections.deque(data)
        return creat_t(None, data)




#2
class Codec2:
    def serialize(self, root):
        if not root:
            return None
        stack = collections.deque()
        stack.append(root)
        ans = []
        while stack:
            for _ in range(len(stack)):
                node = stack.popleft()
                if not node:
                    ans.append('n')
                    continue
                ans.append(str(node.val))
                stack.append(node.left)
                stack.append(node.right)
        return '.'.join(ans)

    def deserialize(self, data):
        if not data:
            return None
        node_val = []
        value = 0
        stack = collections.deque()
        minus = False
        for char in data:
            if char == 'n':
                value = char
            elif char == '.':
                if minus:
                    value = -value
                    minus = False
                node_val.append(value)
                value = 0
            elif char == '-':
                minus = True
            else:
                value = 10 * value + int(char)
        node_val.append(value)
        head = TreeNode(int(node_val[0]))
        stack.append(head)
        index = 0
        n = len(node_val)
        while stack:
            node = stack.popleft()
            index += 1
            if index == n:
                break
            if node_val[index] != 'n':
                node.left = TreeNode(node_val[index])
                stack.append(node.left)
            index += 1
            if index == n:
                break
            if node_val[index] != 'n':
                node.right = TreeNode(node_val[index])
                stack.append(node.right)
        return head

liss = [1, 2, None,None,3,4,None,None,5]
#root = creat_tree(None, liss)
s = Codec()
a = s.serialize(None)
r = s.deserialize(a)
print(0)
