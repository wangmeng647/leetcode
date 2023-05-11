
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        i = 1
        while True:
            ans |= (1 & n)
            n >>= 1
            if i == 32:
                return ans
            ans <<= 1
            i += 1

class Solution2:
    def reverseBits(self, n: int) -> int:
        mask1 = 0x55555555
        mask2 = 0x33333333
        mask3 = 0x0f0f0f0f
        mask4 = 0x00ff00ff
        mask5 = 0x0000ffff
        n = (n & mask1) << 1 | n >> 1 & mask1
        n = (n & mask2) << 2 | n >> 2 & mask2
        n = (n & mask3) << 4 | n >> 4 & mask3
        n = (n & mask4) << 8 | n >> 8 & mask4
        n = (n & mask5) << 16 | n >> 16 & mask5
        return n

class Solution1:
    def reverseBits(self, n: int) -> int:
        mask = 1
        ans = 0
        for _ in range(32):
            ans <<= 1
            ans = ans | (n & mask)
            n >>= 1
        return ans

n = 43261596
s = Solution2()
print(s.reverseBits(n))
