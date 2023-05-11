import collections
import functools

#超时dfs
class Solution:
    def canPartition(self, nums) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        remainder = int(total / 2)
        def dfs(remainder, nums):
            if remainder == 0:
                return True
            if remainder < 0:
                return False
            r = False
            for i in range(len(nums)):
                r_i = dfs(remainder - nums[i], nums[0:i] + nums[i + 1:len(nums)])
                r = r or r_i
            return r
        return dfs(remainder, nums)

class Solution2:
    def canPartition(self, nums) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = int(total / 2)
        n = target + 1
        dp = [False] * n
        dp[0] = True
        for number in nums:
            if dp[-1] is True:
                return True
            for j in reversed(range(n)):
                if j - number >= 0:
                    dp[j] = dp[j - number] or dp[j]
        return dp[-1]




#2
class Solution3:
    def canPartition(self, nums) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        aim = total // 2
        dp = [False] * (aim + 1)
        for i in range(len(nums)):
            dp[0] = True
        for i in range(len(nums)):
            for j in reversed(range(1, aim + 1)):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]]
        return dp[-1]

s = Solution3()
nums = [1,5,10,6]
print(s.canPartition(nums))

class Solution4:
    def canPartition(self, nums) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False
        m, n = len(nums) + 1, sum_ // 2 + 1
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            if dp[-1][-1] == 1:
                return True
            for j in range(1, n):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]]
                dp[i][j] = dp[i][j] or dp[i - 1][j]
        return True if dp[-1][-1] == 1 else False


class Solution5:
    def canPartition(self, nums) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        target = sum_nums // 2
        m, n = len(nums) + 1, target + 1
        dp = [0] * n
        dp[0] = 1
        for i in range(1, m):
            for j in reversed(range(1, n)):
                if j - nums[i - 1] >= 0:
                    dp[j] = dp[j - nums[i - 1]] or dp[j]
        return dp[-1] == 1
