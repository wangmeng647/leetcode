
class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum = nums[0]
        pre = nums[0]
        for i in nums[1:]:
            f = max(i, i + pre)
            max_sum = max(f, max_sum)
            pre = f
        return max_sum





#2
class Solution1:
    def maxSubArray(self, nums) -> int:
        pre = nums[0]
        max_sum = pre
        for n in nums[1:]:
            pre_max = max(n, n + pre)
            max_sum = max(max_sum, pre_max)
            pre = pre_max
        return max_sum



class Solution2:
    def maxSubArray(self, nums) -> int:
        pre = nums[0]
        max_sum = pre
        for n in nums[1:]:
            pre = max(pre, pre + n)
            max_sum = max(max_sum, pre)
        return max_sum



class Solution3:
    def maxSubArray(self, nums) -> int:
        _max = nums[0]
        sub_sum = _max
        for n in nums[1:]:
            sub_sum = max(n, n + sub_sum)
            if sub_sum > _max:
                _max = sub_sum
        return _max



class Solution4:
    def maxSubArray(self, nums) -> int:
        mx = -float('inf')
        large = -float('inf')
        for n in nums:
            large = max(large + n, n)
            mx = max(mx, large)
        return mx
nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution4()
a = s.maxSubArray(nums)
print(a)