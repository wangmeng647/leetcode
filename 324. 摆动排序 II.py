
class Solution:
    def wiggleSort(self, nums) -> None:
        nums.sort()
        n = len(nums)
        if n % 2 == 0:
            index = n // 2
        else:
            index = n // 2 + 1
        sort_nums = nums[:]
        index_l = index - 1
        index_r = n - 1
        i = 0
        while True:
            nums[i] = sort_nums[index_l]
            if i == n - 1:
                break
            i += 1
            index_l -= 1
            nums[i] = sort_nums[index_r]
            if i == n - 1:
                break
            i += 1
            index_r -= 1
        return nums




#2
class Solution2:
    def wiggleSort(self, nums) -> None:
        nums.sort()
        n = len(nums)
        co_nums = nums[:]
        index_r = n - 1
        if n % 2 == 0:
            index_l = n // 2 - 1
        else:
            index_l = n // 2
        for i in range(n):
            if i % 2 == 0:
                nums[i] = co_nums[index_l]
                index_l -= 1
            else:
                nums[i] = co_nums[index_r]
                index_r -= 1
        return nums

s = Solution2()
nums = [4,5,5,6]
print(s.wiggleSort(nums))