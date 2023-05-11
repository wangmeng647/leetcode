
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        n = len(strs)
        ans = ''
        j = 0
        same = True
        while True:
            for i in range(0, n):
                try:
                    if strs[i][j] != strs[0][j]:
                        same = False
                except:
                    same = False
                    break
            if same == False:
                return ans
            ans += strs[0][j]
            j += 1




























class Solution1:
    def longestCommonPrefix(self, strs) -> str:
        ans = ''
        j = 0
        n = len(strs)
        check = False
        while True:
            for i in range(n):
                try:
                    if strs[0][j] == strs[i][j]:
                        check = True
                    else:
                        return ans
                except:
                    return ans
            if check == True:
                ans += strs[0][j]
                j += 1
            else:
                return ans



strs = [""]
s = Solution()
print(s.longestCommonPrefix(strs))





















