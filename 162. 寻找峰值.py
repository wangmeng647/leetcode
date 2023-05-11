

class Solution:
    def findPeakElement(self, nums) -> int:
        n = len(nums)
        l, r = 0, n - 1
        if n == 1:
            return 0
        while True:
            mid = (l + r) // 2
            if mid == 0 and nums[mid] > nums[mid + 1] or mid == n - 1 and nums[mid] > nums[mid - 1]\
                    or nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif mid == 0 and nums[mid] < nums[mid + 1] or nums[mid - 1] < nums[mid] < nums[mid + 1]:
                l = mid + 1
            elif mid == n - 1 and nums[mid] < nums[mid - 1] or nums[mid - 1] > nums[mid] > nums[mid + 1]:
                r = mid - 1
            elif nums[mid - 1] > nums[mid] < nums[mid + 1]:
                r = mid - 1



#2
class Solution2:
    def findPeakElement(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return 0
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if (mid == 0 and nums[0] > nums[1]) or (mid == n - 1 and nums[n - 2] < nums[n - 1]):
                return mid
            elif nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] < nums[mid] < nums[mid + 1] or (mid == 0 and nums[mid] < nums[mid + 1]):
                l = mid + 1
            elif nums[mid - 1] > nums[mid] > nums[mid + 1] or (mid == n - 1 and nums[mid] < nums[mid - 1]):
                r = mid - 1
            else:
                l = mid + 1
        return r
nums = [1,0, 2]
s = Solution2()
print(s.findPeakElement(nums))
