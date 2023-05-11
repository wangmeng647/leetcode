

class Solution:
    def jump(self, nums) -> int:
        dp = [len(nums)] * len(nums)
        dp[0] = 0
        for i in range(len(nums) - 1):
            if dp[i] == len(nums):
                continue
            for j in range(1, 1 + nums[i]):
                if i + j >= len(nums):
                    continue
                dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[-1]

s = Solution()
nums = [2,1]
print(s.jump(nums))