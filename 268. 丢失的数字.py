import collections


class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        dic = collections.defaultdict(int)
        for nu in nums:
            dic[nu] = 1
        for key in range(n + 1):
            if dic[key] == 0:
                return key