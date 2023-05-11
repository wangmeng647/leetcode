import copy


class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0
        n = total * 2 + 1
        dp = [0] * n
        dp[nums[0] + total] = 1
        dp[-nums[0] + total] += 1
        for number in nums[1:]:
            dp_cache = [0] * n
            for i in range(n):
                if i - total - number >= -total and i - total + number <= total:
                    dp_cache[i - number] += dp[i]
                    dp_cache[i + number] += dp[i]
            dp = copy.copy(dp_cache)
        return dp[target + total]

class Solution2:
    def findTargetSumWays(self, nums, target: int) -> int:
        if (sum(nums) - target) % 2 == 1 or sum(nums) < target:
            return 0
        neg = int((sum(nums) - target) / 2)
        dp = [1] + [0] * neg
        for nu in nums:
            for j in reversed(range(neg + 1)):
                if j >= nu:
                    dp[j] = dp[j] + dp[j - nu]
        return dp[neg]






#2
class Solution3:
    def findTargetSumWays(self, nums, target: int):
        total = sum(nums)
        if target > total or target < -total:
            return 0
        m = len(nums)
        n = 2 * total + 1
        dp = [[0] * n for _ in range(m)]
        dp[0][total - nums[0]] += 1
        dp[0][total + nums[0]] += 1
        for i in range(1, m):
            for j in range(n):
                if j - nums[i] >= 0:
                    dp[i][j] += dp[i - 1][j - nums[i]]
                if j + nums[i] < n:
                    dp[i][j] += dp[i - 1][j + nums[i]]
        return dp[-1][target + total]


class Solution4:
    def findTargetSumWays(self, nums, target: int):
        if (sum(nums) - target) % 2 == 1 or sum(nums) < target:
            return 0
        neg = int((sum(nums) - target) / 2)
        dp = [[0] * (neg + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(neg + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]




class Solution5:
    def findTargetSumWays(self, nums, target: int) -> int:
        total_sum = sum(nums)
        if (total_sum + target) % 2 == 1:
            return 0
        positive = int((total_sum + target) / 2)
        if positive < 0:
            return 0
        m, n = len(nums) + 1, positive + 1
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(n):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

nums = [100]
#nums = [0,0,0,0,0,0,0,0]
target = -200
s = Solution5()
print(s.findTargetSumWays(nums, target))