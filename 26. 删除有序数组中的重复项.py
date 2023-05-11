
class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 1:
            return 1
        index_l = 0
        index_r = 1
        while True:
            n = len(nums)
            if index_r < n:
                if nums[index_r] == nums[index_l]:
                    nums.pop(index_r)
                else:
                    index_l = index_r
                    if index_r < n - 1:
                        index_r += 1
                    else:
                        return index_r + 1
            else:
                return index_r

s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums))