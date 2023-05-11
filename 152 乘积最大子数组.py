
class Solution:
    def maxProduct(self, nums) -> int:
        max_mul = nums[0]
        pre_max, pre_min = nums[0], nums[0]
        for i in nums[1:]:
            f_max = max(pre_max * i, pre_min * i, i)
            f_min = min(pre_max * i, pre_min * i, i)
            pre_max = f_max
            pre_min = f_min
            max_mul = max(max_mul, f_max)
        return max_mul







#2
class Solution2:
    def maxProduct(self, nums) -> int:
        max_sum = nums[0]
        pre_max = pre_min = nums[0]
        for n in nums[1:]:
            pre_max, pre_min = max(pre_max * n, pre_min * n, n), min(pre_max * n, pre_min * n, n)
            max_sum = max(max_sum, pre_max)
        return max_sum


s = Solution2()
nums = [-4,-3,-2]
print(s.maxProduct(nums))