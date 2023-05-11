import functools

class Solution:
    def maxCoins(self, nums) -> int:
        n = len(nums)
        val = [1] + nums + [1]

        @functools.lru_cache(None)
        def solve(left: int, right: int) -> int:
            if left >= right - 1:
                return 0

            best = 0
            for i in range(left + 1, right):
                total = val[left] * val[i] * val[right]
                total += solve(left, i) + solve(i, right)
                best = max(best, total)

            return best

        return solve(0, n + 1)


class Solution2:
    def maxCoins(self, nums) -> int:
        n = len(nums)
        rec = [[0] * (n + 2) for _ in range(n + 2)]
        val = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += rec[i][k] + rec[k][j]
                    rec[i][j] = max(rec[i][j], total)

        return rec[0][n + 1]

class Solution3:
    def maxCoins(self, nums) -> int:

        #nums首尾添加1，方便处理边界情况
        nums.insert(0,1)
        nums.insert(len(nums),1)

        store = [[0]*(len(nums)) for i in range(len(nums))]

        def range_best(i,j):
            m = 0
            #k是(i,j)区间内最后一个被戳的气球
            for k in range(i+1,j): #k取值在(i,j)开区间中
                #以下都是开区间(i,k), (k,j)
                left = store[i][k]
                right = store[k][j]
                a = left + nums[i]*nums[k]*nums[j] + right
                if a > m:
                    m = a
            store[i][j] = m

        #对每一个区间长度进行循环
        for n in range(2,len(nums)): #区间长度 #长度从3开始，n从2开始
            #开区间长度会从3一直到len(nums)
            #因为这里取的是range，所以最后一个数字是len(nums)-1

            #对于每一个区间长度，循环区间开头的i
            for i in range(0,len(nums)-n): #i+n = len(nums)-1

                #计算这个区间的最多金币
                range_best(i,i+n)

        return store[0][len(nums)-1]









class Solution4:
    def maxCoins(self, nums) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        cache = [[0] * n for _ in range(n)]
        def update_max(start, end):
            max_reward = 0
            for k in range(start + 1, end):
                reward = cache[start][k] + cache[k][end] + nums[k] * nums[start] * nums[end]
                max_reward = max(max_reward, reward)
                cache[start][end] = max_reward
        for length in range(1, n - 1):
            for begin in range(0, n - length - 1):
                update_max(begin, begin + length + 1)
        return cache[0][n - 1]



#2
class Solution5:
    def maxCoins(self, nums) -> int:
        def max_dp(i, j):
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for l in range(1, n - 1):
            for i in range(0, n - 2):
                if i + 1 + l > n - 1:
                    continue
                max_dp(i, i + l + 1)
        return dp[0][n - 1]

nums = [3,1,5,8]
s = Solution5()
print(s.maxCoins(nums))









