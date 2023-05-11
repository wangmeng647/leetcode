

class Solution:
    def increasingTriplet(self, nums) -> bool:
        first = nums[0]
        second = float('inf')
        for n in nums[1:]:
            if n > second:
                return True
            if n > first:
                second = n
            if n < first:
                first = n
        return False




#2
class Solution2:
    def increasingTriplet(self, nums) -> bool:
        first = nums[0]
        second = float('inf')
        for n in nums:
            if n > second:
                return True
            if n > first:
                second = n
            else:
                first = n
        return False

nums = [2,1,5,0,4,6]
s = Solution2()
print(s.increasingTriplet(nums))