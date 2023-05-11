class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        ans = []
        for num in nums:
            nums[abs(num)-1] = -abs(nums[abs(num) - 1])
        for i in range(n):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans
nums = [4,3,2,7,8,2,3,1]
s = Solution()
print(s.findDisappearedNumbers(nums))