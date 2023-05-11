
class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        max_num = 0
        min_num = float('inf')
        l, r = 0, -1
        n = len(nums)
        for i in range(n):
            max_num = max(max_num, nums[i])
            if nums[i] < max_num:
                r = i
            min_num = min(min_num, nums[n - i - 1])
            if nums[n - i - 1] > min_num:
                l = n - i - 1
        return r - l + 1



#2
class Solution2:
    def findUnsortedSubarray(self, nums):
        l, r = 1, 0
        n = len(nums)
        biggest, smallest = -float('inf'), float('inf')
        for i in range(n):
            biggest = max(biggest, nums[i])
            if nums[i] < biggest:
                r = i
            smallest = min(smallest, nums[n - i - 1])
            if smallest < nums[n - i - 1]:
                l = n - i - 1
        return r - l + 1

s = Solution2()
nums = [-1,-1,-1,-1]
print(s.findUnsortedSubarray(nums))