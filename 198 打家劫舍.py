class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        p = nums[0]
        q = max(nums[1], p)
        for i in nums[2:]:
            r = max(i + p, p, q)
            p = q
            q = r
        return r




#2
class Solution2:
    def rob(self, nums) -> int:
        stole = nums[0]
        un_stole = 0
        for p in nums[1:]:
            un_stole, stole = stole, max(stole, un_stole + p)
        return stole


class Solution3:
    def rob(self, nums):
        steal = 0
        un_steal = 0
        for n in nums:
            p = steal
            steal = un_steal + n
            un_steal = max(un_steal, p)
        return max(un_steal, steal)



class Solution4:
    def rob(self, nums) -> int:
        steal = nums[0]
        un_steal = 0
        for n in nums[1:]:
            cache = steal
            steal = un_steal + n
            un_steal = max(un_steal, cache)
        return max(un_steal, steal)
lis = [2,1,1,2]
s = Solution4()
print(s.rob(lis))