
class Solution:
    def findDuplicate(self, nums) -> int:
        f = s = nums[0]
        while True:
            f = nums[nums[f]]
            s = nums[s]
            if f == nums[0]:
                return f
            if f == s:
                break
        pre = nums[0]
        while True:
            pre = nums[pre]
            s = nums[s]
            if pre == s:
                return s