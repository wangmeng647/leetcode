
class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return list()
        n = len(digits)
        index = 0
        phone = {'2': 'abc',
         '3': 'def',
         '4': 'ghi',
         '5': 'jkl',
         '6': 'mno',
         '7': 'pqrs',
         '8': 'tuv',
         '9': 'wxyz'}
        words = []
        combination = []
        def backtrack(index):
            if index == n:
                combination.append("".join(words))
            else:
                for letter in phone[digits[index]]:
                    words.append(letter)
                    backtrack(index +1)
                    words.pop()
        backtrack(index)
        return combination


#2
class Solution1:
    def letterCombinations(self, digits: str):
        phone = {'2': 'abc',
                 '3': 'def',
                 '4': 'ghi',
                 '5': 'jkl',
                 '6': 'mno',
                 '7': 'pqrs',
                 '8': 'tuv',
                 '9': 'wxyz'}
        ans = []
        combination = []
        def dfs(index):
            if index == len(digits):
                ans.append(''.join(combination))
                return
            for ss in phone[digits[index]]:
                combination.append(ss)
                dfs(index + 1)
                combination.pop()
        dfs(0)
        return ans

digits = "23"
s = Solution()
print(s.letterCombinations(digits))