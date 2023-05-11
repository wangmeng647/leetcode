

class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        aim = n - 1
        for i in reversed(range(n - 1)):
            if nums[i] >= aim - i:
                aim = i
        return aim == 0

s = Solution()
nums = [3,2,1,0,4]
print(s.canJump(nums))


#2
class Solution2:
    def canJump(self, nums) -> bool:
        nums = nums[::-1]
        min_step = 1
        for i in range(1, len(nums)):
            if nums[i] >= min_step:
                min_step = 1
            else:
                min_step += 1
        return min_step == 1