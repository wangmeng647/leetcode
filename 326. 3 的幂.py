import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        while True:
            remain = n % 3
            if remain != 0:
                return False
            quotient = n // 3
            if quotient == 1:
                return True
            n = quotient