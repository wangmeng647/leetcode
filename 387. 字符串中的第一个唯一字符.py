import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = collections.defaultdict(int)
        for sub_s in s:
            dic[sub_s] += 1

        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1




class Solution1:
    def firstUniqChar(self, s: str) -> int:
        counts = collections.defaultdict(int)
        for ss in s:
            counts[ss] += 1
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        return -1