
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        total = 0
        for i in range(n):
            total += 26 ** i * (ord(columnTitle[n - 1 - i]) - 96)
        return total