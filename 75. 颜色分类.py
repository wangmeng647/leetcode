
class Solution:
    def sortColors(self, nums) -> None:
        index = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
        for j in range(n):
            if nums[j] == 1:
                nums[j], nums[index] = nums[index], nums[j]
                index += 1
        return nums



#2
class Solution2:
    def sortColors(self, nums) -> None:
        l, r = 0, len(nums) - 1
        index = 0
        while index <= r:
            while nums[index] == 2:
                if r == index:
                    return nums
                nums[index], nums[r] = nums[r], nums[index]
                r -= 1
            if nums[index] == 0:
                nums[index], nums[l] = nums[l], nums[index]
                l += 1
            index += 1
        return nums

nums = [2]
s = Solution2()
print(s.sortColors(nums))