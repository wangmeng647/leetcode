
class Solution:
    def moveZeroes(self, nums) -> None:
        r = l = 0
        n = len(nums)
        while r < n:
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        return nums



#2
class Solution2:
    def moveZeroes(self, nums) -> None:
        l = r = 0
        n = len(nums)
        while r < n:
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        return nums



nums = [0,1,0,3,12]
s = Solution2()
print(s.moveZeroes(nums))