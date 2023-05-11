
class Solution:
    def plusOne(self, digits):
        n = len(digits)
        ans = []
        carry = 0
        for i in reversed(range(n)):
            add = digits[i] + carry
            if add > 9:
                carry = 1
                ans.append(0)
            else:
                carry = 0
                ans.append(add)
        if carry == 1:
            ans.append(1)
        ans.reverse()
        return ans






















class Solution1:
    def plusOne(self, digits):
        carry = 1
        n = len(digits)
        for i in reversed(range(n)):
            if carry == 1 and digits[i] + 1 == 10:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = digits[i] + 1
                carry = 0
                break
        if carry == 1:
            return [1] + [0] * n
        else:
            return digits