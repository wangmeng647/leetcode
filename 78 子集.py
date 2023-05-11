import copy


class Solution:
    def subsets(self, nums):
        ans = [[]]
        for n in nums:
            for i in range(len(ans)):
                ans.append(ans[i] + [n])
        return ans




#2
class Solution2:
    def subsets(self, nums):
        ans = []
        cache = []
        def dfs(index):
            if index == len(nums):
                ans.append(copy.copy(cache))
                return
            cache.append(nums[index])
            dfs(index + 1)
            cache.pop()
            dfs(index + 1)
        dfs(0)
        return ans

s = Solution2()
nums = [1,2,3]
print(s.subsets(nums))