
class Solution:
    def rotate(self, nums, k: int) -> None:
        k = k % len(nums)
        if k == 0:
            return nums
        nums.reverse()
        nums[0:k] = nums[k - 1::-1]
        nums[k:] = nums[len(nums) - 1:k - 1:-1]
        return nums

class Solution2:
    def rotate(self, nums, k: int) -> None:
        if len(nums) == 1 or k == 0 or k == len(nums):
            return nums
        def gcd(num1, num2):
            a = max(num1, num2)
            b = min(num1, num2)
            while a != b:
                c = a % b
                if c == 0:
                    return b
                a = b
                b = c
        n = len(nums)
        g = gcd(n, k)
        for i in range(g):
            start = i
            index = k + i
            temp1 = nums[start]
            while True:
                index = index % n
                temp2 = nums[index]
                nums[index] = temp1
                if index == start:
                    break
                temp1 = temp2
                index += k
        return nums






#2
class Solution3:
    def rotate(self, nums, k: int) -> None:
        def gcd(x, y):
            m, n = max(x, y), min(x, y)
            while True:
                r = m % n
                if r == 0:
                    return n
                m, n = n, r
        if k == 0:
            return nums
        n = len(nums)
        div = gcd(n, k)
        for i in range(div):
            index = i
            cache1 = nums[index]
            while True:
                index %= n
                cache2 = nums[(index + k) % n]
                nums[(index + k) % n] = cache1
                if (index + k) % n == i:
                    break
                cache1 = cache2
                index += k
        return nums

nums = [1]
k = 0
s = Solution3()
print(s.rotate(nums, k))