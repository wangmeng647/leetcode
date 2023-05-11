
class BIT:
    def __init__(self, nums):
        self.nums = nums
        self.sum = [0] * (len(nums) + 1)
        self.initial()
    def initial(self):
        n = len(self.nums)
        for i in range(n):
            index = i + 1
            while index < n + 1:
                self.sum[index] += self.nums[i]
                index += (-index) & index

    def add(self, i, x):
        self.nums[i] += x
        i += 1
        while i < len(self.nums) + 1:
            self.sum[i] += x
            i += (-i) & i

    def query(self, i):
        i += 1
        ans = 0
        while i > 0:
            ans += self.sum[i]
            i -= (-i) & i
        return ans

nums = [1,2,3,4,5,6,7,8]
s = BIT(nums)
s.add(1, 3)
print(s.query(4))