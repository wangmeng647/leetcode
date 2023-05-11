import collections


class Solution:
    def subarraySum(self, nums, k):
        counts = 0
        maps = {}
        maps[0] = 1
        pre = 0
        for x in nums:
            pre += x
            if pre - k in maps:
                counts += maps[pre - k]
            if pre not in maps:
                maps[pre] = 1
            else:
                maps[pre] += 1
        return counts


#bruteforce overtime
class Solution2:
    def subarraySum(self, nums, k):
        counts = 0
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                if s == k:
                    counts += 1
        return counts

class Solution3:
    def subarraySum(self, nums, k):
        mp = collections.defaultdict(int)
        pre = 0
        counts = 0
        mp[0] = 1
        for n in nums:
            pre += n
            if pre - k in mp:
                counts += mp[pre - k]
            mp[pre] += 1
        return counts

nums = [-1,1,0,0]
nums = [0,0,0]
k = 0
s = Solution3()
print(s.subarraySum(nums, k))

