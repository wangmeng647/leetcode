import copy
class Solution:
    def permute(self, nums):
        self.ans = []
        array = []
        def dfs(nums, array):
            if not nums:
                self.ans.append(copy.copy(array))
                return
            n = len(nums)
            for i in range(len(nums)):
                array.append(nums[i])
                dfs(nums[0:i]+nums[i + 1: n], array)
                array.pop(-1)
        dfs(nums, array)
        return self.ans

'''s = Solution()
nums = [0, 1]
print(s.permute(nums))'''

#2
class Solution1:
    def permute(self, nums):
        ans = []
        combination = []
        def dfs(nums):
            if not nums:
                ans.append(copy.copy(combination))
                return
            for i in range(len(nums)):
                combination.append(nums[i])
                dfs(nums[0:i] + nums[i + 1:])
                combination.pop()
        dfs(nums)
        return ans

s = Solution1()
nums = [1, 2, 3]
print(s.permute(nums))