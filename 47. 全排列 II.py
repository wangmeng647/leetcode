import collections
import copy


class Solution:
    def permuteUnique(self, nums):
        n = len(nums)
        nums = collections.Counter(nums)
        combination = []
        ans = []
        def dfs(pre):
            if len(combination) == n:
                ans.append(copy.deepcopy(combination))
                return
            for k, v in nums.items():
                if k == pre:
                    continue
                for i in range(1, v + 1):
                    combination.append(k)
                    nums[k] -= 1
                    dfs(k)
                while v > 0:
                    combination.pop()
                    nums[k] += 1
                    v -= 1
        dfs(11)
        return ans



class Solution2:
    def permuteUnique(self, nums):
        ans = set()
        combination = []

        def dfs(num):
            if len(num) == 0:
                ans.add(tuple(combination[:]))
                return

            for i in range(len(num)):
                combination.append(num[i])
                dfs(num[:i] + num[i + 1:])
                combination.pop()
        dfs(nums)
        return [list(a) for a in ans]


class Solution3:
    def permuteUnique(self, nums):
        fre = collections.Counter(nums)
        ans = []
        combination = []

        def dfs(pre):
            nonlocal combination
            if len(combination) == len(nums):
                ans.append(combination[:])
                return
            for k, v in fre.items():
                if pre == k:
                    continue
                for i in range(v):
                    combination.append(k)
                    fre[k] -= 1
                    dfs(k)
                combination = combination[:len(combination) - v]
                fre[k] += v
        dfs(0.1)
        return ans

s = Solution3()
nums = [1,1,2]
res = s.permuteUnique(nums)
print(res)
