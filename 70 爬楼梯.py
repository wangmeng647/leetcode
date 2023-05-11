
class Solution:
    def climbStairs(self, n: int) -> int:
        q = 0
        r = 1
        for i in range(n):
            p = q
            q = r
            r = p + q
        return r








class Solution1:
    def climbStairs(self, n: int) -> int:
        y = 0
        z = 1
        for i in range(n):
            x = y
            y = z
            z = x + y
        return z




class Solution2:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        p1 = 1
        p2 = 2
        p3 = 4
        p = 0
        for i in range(4, n + 1):
            p = p1 + p2 + p3
            p1 = p2
            p2 = p3
            p3 = p
        return p % 1000000007


class Solution3:
    def climbStairs(self, n: int):
        nums = [1, 2]
        ans = []
        combination = []
        def dfs(idx, remain):
            if remain == 0:
                ans.append(combination[:])
                return
            if idx == len(nums):
                return
            if remain < nums[idx]:
                return
            combination.append(nums[idx])
            dfs(idx, remain - nums[idx])
            combination.pop()
            dfs(idx + 1, remain)
        dfs(0, n)
        return ans

class Solution4:
    def climbStairs(self, n: int):
        nums = [1, 2]
        ans = []
        combination = []
        def dfs(remain):
            if remain == 0:
                ans.append(combination[:])
                return
            if remain < 0:
                return
            for step in nums:
                combination.append(step)
                dfs(remain - step)
                combination.pop()
        dfs(n)
        return ans

s = Solution4()
res = s.climbStairs(4)
print(res)
print(len(res))
# 4 5  5 8 6  13