
MASK1 = 2 ** 32
MASK2 = 2 ** 32 - 1
MASK3 = 2 ** 31
class Solution:
    def getSum(self, a: int, b: int) -> int:
        a = a % MASK1
        b = b % MASK1
        while True:
            carry = (a & b) << 1
            a = a ^ b
            b = carry % MASK1
            if b == 0:
                if a & MASK3:
                    a = ~a ^ MASK2
                return a




#2
class Solution2:
    def getSum(self, a: int, b: int) -> int:
        a = a % MASK1
        b = b % MASK1
        carry = ((a & b) << 1) % MASK1
        a = a ^ b
        while carry != 0:
            b = a
            a = a ^ carry
            carry = ((carry & b) << 1) % MASK1
        if a > 2 ** 31 - 1:
            a = ~MASK2 | a
        return a

s = Solution2()
print(s.getSum(-3, -7))
