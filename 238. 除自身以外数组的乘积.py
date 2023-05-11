

class Solution:
    def productExceptSelf(self, nums):
        ans = [1]
        n = len(nums)
        mul = 1
        for i in range(n - 1):
            mul *= nums[i]
            ans.append(mul)
        mul = 1
        for i in range(n - 1, 0, -1):
            mul *= nums[i]
            ans[i - 1] *= mul
        return ans




#2
class Solution2:
    def productExceptSelf(self, nums):
        mul = 1
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            mul = mul * nums[i - 1]
            ans[i] = mul
        mul_r = 1
        for i in reversed(range(n - 1)):
            mul_r = nums[i + 1] * mul_r
            ans[i] = mul_r * ans[i]
        return ans




class Solution3:
    def productExceptSelf(self, nums):
        n = len(nums)
        left = [1]
        right = [1] * n
        for i in range(1, n):
            left.append(left[-1] * nums[i - 1])
            right[n - 1 - i] = right[n - i] * nums[n - i]
        ans = []
        for i in range(n):
            ans.append(left[i] * right[i])
        return ans


s = Solution3()
nums = [-1, 1, 2, -3, 3]
print(s.productExceptSelf(nums))