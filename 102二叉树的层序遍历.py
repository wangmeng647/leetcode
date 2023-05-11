import collections
import copy
from creat_tree import creat_tree

class Solution:
    def levelOrder(self, root):
        lis = []
        queue1 = []
        queue2 = []
        queue1.append(root)
        l = []
        while queue1 or queue2:
            while queue1:
                node = queue1.pop(0)
                if node.left is not None:
                    queue2.append(node.left)
                if node.right is not None:
                    queue2.append(node.right)
                l.append(node.val)
            lis.append(l)
            l = []
            while queue2:
                node = queue2.pop(0)
                if node.left is not None:
                    queue1.append(node.left)
                if node.right is not None:
                    queue1.append(node.right)
                l.append(node.val)
            lis.append(l)
            l = []
        return lis




#2
class Solution2:
    def levelOrder(self, root):
        if not root:
            return None
        que = collections.deque()
        cache = []
        ans = []
        que.append(root)
        layer = []
        while True:
            while que:
                node = que.popleft()
                layer.append(node.val)
                if node.left:
                    cache.append(node.left)
                if node.right:
                    cache.append(node.right)
            if not cache:
                ans.append(copy.deepcopy(layer))
                return ans
            ans.append(copy.deepcopy(layer))
            layer.clear()
            que.extend(cache)
            cache.clear()

l = [3,9,20,None,None,15,7]
root = creat_tree(l)
s = Solution2()
print(s.levelOrder(root))