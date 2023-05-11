
class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        for i in range(n):
            if abs(nums[i]) != n + 1:
                nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


class Solution2:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1



nums = [1, 1]
s = Solution()
print(s.firstMissingPositive(nums))

#2
class Solution3:
    def firstMissingPositive(self, nums) -> int:
        has = set()
        for n in nums:
            has.add(n)
        for i in range(1, len(nums) + 2):
            if i not in has:
                return i