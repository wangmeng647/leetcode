


class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                remain = target - nums[i] - nums[j]
                visited = set()
                for p in range(j + 1, len(nums)):
                    if remain - nums[p] in visited:
                        ans.add((nums[i], nums[j], remain - nums[p], nums[p]))
                    visited.add(nums[p])
        return [list(a) for a in ans]
nums = [1,0,-1,0,-2,2]
target = 0
s = Solution()
print(s.fourSum(nums, target))
