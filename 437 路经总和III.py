'''
class Solution1:
    def pathSum(self, root, targetSum: int):
        def rootSum(root, targetSum):
            if root is None:
                return 0
            counts = 0
            if root.val == targetSum:
                counts += 1
            counts += rootSum(root.left, targetSum - root.val)
            counts += rootSum(root.right, targetSum - root.val)
            return counts
        if root is None:
            return 0
        counts = rootSum(root,targetSum)
        counts += self.pathSum(root.left, targetSum)
        counts += self.pathSum(root.right, targetSum)
        return counts
'''

#前缀和
from creat_tree import creat_tree
import collections
class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        dic = collections.defaultdict(int)
        dic[0] = 1
        curr = 0
        def traverse(root, curr):
            if root is None:
                return 0
            ret = 0
            curr += root.val
            #dic[curr] += 1
            if curr - targetSum in dic:
                ret += dic[curr - targetSum]
            dic[curr] += 1
            ret += traverse(root.left, curr)
            ret += traverse(root.right, curr)
            dic[curr] -= 1
            return ret
        return traverse(root, curr)

lis = [10,5,3,None,None,3,-1,1,None,None,None,None,None]
tree = creat_tree(None, lis)
s = Solution()
c = s.pathSum(tree, 8)
print(c)