import functools
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums) -> str:
        l, r = 0, len(nums) - 1
        def compare(num1, num2):
            combine1 = int(num1 + num2)
            combine2 = int(num2 + num1)
            if combine1 > combine2:
                return True
            else:
                return False

        def sort(l, r):
            if l == r:
                return [nums[l]]
            mid = (l + r) // 2
            l1 = sort(l, mid)
            l2 = sort(mid + 1, r)
            result = []
            while l1 and l2:
                if compare(str(l1[0]), str(l2[0])):
                    result.append(l1[0])
                    l1.pop(0)
                else:
                    result.append(l2[0])
                    l2.pop(0)
            if l1:
                return result + l1
            else:
                return result + l2
        result = sort(l, r)
        ans = ''
        for s in result:
            ans += str(s)
        if int(ans) == 0:
            return '0'
        return ans




#2
class Solution2:
    def largestNumber(self, nums) -> str:
        def my_cmp(x, y):
            return int(y + x) - int(x + y)
        ls = sorted(map(str, nums), key=cmp_to_key(my_cmp))
        return '0' if ls[0] == '0' else ''.join(ls)



class Solution3:
    def largestNumber(self, nums) -> str:
        ls = map(str, nums)
        def cmp(x, y):
            return int(y + x) - int(x + y)
        res = sorted(ls, key=cmp_to_key(cmp))
        return '0' if res[0] == '0' else ''.join(res)

s = Solution3()
nums = [3,30,34,5,9]
print(s.largestNumber(nums))