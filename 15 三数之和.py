import collections


class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            sub_target = 0 - nums[i]
            l, r = i + 1, n - 1
            while l < r:
                sub_sum = nums[l] + nums[r]
                if sub_sum == sub_target:
                    if l - 1 > i and nums[l - 1] == nums[l]:
                        l += 1
                        r -= 1
                        continue
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif sub_sum > sub_target:
                    r -= 1
                else:
                    l += 1
        return ans

'''nums = [-1,0,1,2,-1,-4]
s = Solution()
print(s.threeSum(nums))'''

#2
class Solution1:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        ans = []
        dic = set()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            s = -nums[i]
            dic.clear()
            r = True
            for j in range(i + 1, n):
                if r and nums[j] == s / 2 and nums[j] == nums[j - 1] and j > i + 1:
                    r = False
                    ans.append((nums[i], s - nums[j], nums[j]))
                    continue
                elif j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if s - nums[j] in dic:
                    ans.append((nums[i], s - nums[j], nums[j]))
                dic.add(nums[j])
        return ans



class Solution2:
    def threeSum(self, nums):
        nums.sort()
        ans = set()
        n = len(nums)
        for i in range(n):
            target = -nums[i]
            if target < 0:
                break
            visited = set()
            for j in range(i + 1, n):
                if target - nums[j] in visited:
                    ans.add((-target, target - nums[j], nums[j]))
                    continue
                visited.add(nums[j])
        ans = list(ans)
        for i in range(len(ans)):
            ans[i] = list(ans[i])
        return ans

#nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
#nums = [0,0,0,0]


class Solution3:
    def threeSum(self, nums):
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            target = -nums[i]
            if target < 0:
                break
            visited = set()
            for j in range(i + 1, len(nums)):
                if target - nums[j] in visited:
                    ans.add((-target, target - nums[j], nums[j]))
                visited.add(nums[j])
        return [list(c) for c in ans]
nums = [-1,0,1,2,-1,-4]
s = Solution3()
print(s.threeSum(nums))
