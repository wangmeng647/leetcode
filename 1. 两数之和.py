
class Solution:
    def twoSum(self, nums, target: int):
        dic = {}
        n = len(nums)
        for i in range(1, n):
            if target - nums[i] in dic:
                return [dic[target - nums[i]], i]
            dic[nums[i]] = i


        hash = {}
        for i, num in enumerate(nums):
            if target - num in hash:
                return [i, hash[target - num]]
            hash[num] = i
        return []

