

class Solution:
    def rob(self, nums) -> int:
        steal_1 = nums[0]
        un_steal_1 = nums[0]
        steal_2 = 0
        un_steal_2 = 0
        for i in range(1, len(nums)):
            if i >= 2:
                ca_s1 = steal_1
                steal_1 = un_steal_1 + nums[i]
                un_steal_1 = max(ca_s1, un_steal_1)
            ca_s2 = steal_2
            steal_2 = un_steal_2 + nums[i]
            un_steal_2 = max(ca_s2, un_steal_2)
        return max(un_steal_1, steal_2, un_steal_2)
nums = [2,3,2]
s = Solution()
print(s.rob(nums))