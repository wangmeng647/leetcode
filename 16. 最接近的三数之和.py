

class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        min_differ = float('inf')
        max_close = 0
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            remain = target - nums[i]
            while l < r:
                if nums[l] + nums[r] == remain:
                    return target
                if nums[l] + nums[r] < remain:
                    if min_differ > remain - nums[l] - nums[r]:
                        min_differ = remain - nums[l] - nums[r]
                        max_close = nums[i] + nums[l] + nums[r]
                    l += 1
                else:
                    if min_differ > abs(remain - nums[l] - nums[r]):
                        min_differ = abs(remain - nums[l] - nums[r])
                        max_close = nums[i] + nums[l] + nums[r]
                    r -= 1
        return max_close
s = Solution()
nums = [-1,2,1,-4]
target = 1
print(s.threeSumClosest(nums, target))


