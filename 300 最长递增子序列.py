class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        table = [1] * n
        for i in range(n):
            max_len = 1
            for j in range(i + 1):
                if nums[j] < nums[i]:
                    max_len = max(max_len, table[j] + 1)
            table[i] = max_len
        return max(table)

#长度最小值 + 二分查找
class Solution1:
    def lengthOfLIS(self, nums) -> int:
        table = [nums[0]]
        for n in nums[1:]:
            if n > table[-1]:
                table.append(n)
            else:
                lo, hi = 0, len(table) - 1
                while True:
                    mid = (lo + hi) // 2
                    if n <= table[mid]:
                        hi = mid
                        if lo == hi:
                            table[lo] = n
                            break
                    else:
                        lo = mid
                        if lo + 1 == hi:
                            table[hi] = n
                            break
        return len(table)



#2
class Solution2:
    def lengthOfLIS(self, nums) -> int:
        dp = [1] * len(nums)
        n = len(nums)
        max_l = 1
        for i in range(1, n):
            max_i = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    max_i = max(max_i, dp[j] + 1)
            dp[i] = max_i
            max_l = max(max_i, max_l)
        return max_l

class Solution3:
    def lengthOfLIS(self, nums) -> int:
        dp = [1] * len(nums)
        for i in range(1 , len(nums)):
            max_l = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    max_l = max(max_l, dp[j] + 1)
            dp[i] = max_l
        return max(dp)

class Solution4:
    def lengthOfLIS(self, nums) -> int:
        ls = [nums[0]]
        for n in nums[1:]:
            if n > ls[-1]:
                ls.append(n)
            else:
                l, r = 0, len(ls) - 1
                while True:
                    mid = (l + r) // 2
                    if n <= ls[mid]:
                        r = mid
                        if l == r:
                            ls[r] = n
                            break
                    else:
                        l = mid
                        if l + 1 == r:
                            ls[r] = n
                            break
        return len(ls)


class Solution5:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            mx = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    mx = max(mx, dp[j] + 1)
            dp[i] = mx
        return max(dp)
nums = [1,3,6,7,9,4,10,5,6]

s = Solution5()
print(s.lengthOfLIS(nums))