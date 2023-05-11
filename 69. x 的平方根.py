
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        l = 0
        r = x
        while True:
            mid = (l + r) // 2
            if mid * mid > x:
                if mid == l + 1:
                    return l
                r = mid

            elif mid * mid < x:
                if mid + 1 == r:
                    return mid
                l = mid

            elif mid * mid == x:
                return mid

class Solution1:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        i = x
        while True:
            i_next = i / 2 + x / 2 / i
            if i - i_next < 1e-5:
                break
            i = i_next
        return int(i)










class Solution2:
    def mySqrt(self, x: int) -> int:
        i = x
        if x == 0:
            return x
        while True:
            i_next = i / 2 + x / 2 / i
            if i - i_next < 1e-5:
                break
            i = i_next
        return int(i)










