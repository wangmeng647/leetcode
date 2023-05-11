
class Solution:
    def nextPermutation(self, nums) -> None:
        n = len(nums)
        for i in reversed(range(n)):
            if i == 0:
                return nums.reverse()
            if nums[i - 1] < nums[i]:
                break
        for j in reversed(range(n)):
            if nums[i - 1] < nums[j]:
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                break
        l, r = i, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums


#2
class Solution2:
    def nextPermutation(self, nums) -> None:
        n = len(nums)
        i = n
        for i in reversed(range(n)):
            if i == 0:
                break
            if nums[i - 1] < nums[i]:
                break
        if i == 0:
            nums.reverse()
            return
        for j in reversed(range(n)):
            if nums[j] > nums[i - 1]:
                nums[j], nums[i - 1] = nums[i - 1], nums[j]
                break
        l, r = i, n - 1
        while l < r:
            nums[l],nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums

nums = [1,2,5,4,3]
s = Solution2()
print(s.nextPermutation(nums))
