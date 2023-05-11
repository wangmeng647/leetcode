


class Solution:
    def minimizeArrayValue(self, nums) -> int:
        for i in reversed(range(1, len(nums))):
            if nums[i] > nums[i - 1]:
                n_1 = n_2 = (nums[i] + nums[i - 1]) // 2
                if (nums[i] + nums[i - 1]) % 2 != 0:
                    n_1 += 1
                nums[i] = n_2
                nums[i - 1] = n_1
        return max(nums)

s = Solution()
nums = [3,7,1,6]
print(s.minimizeArrayValue(nums))