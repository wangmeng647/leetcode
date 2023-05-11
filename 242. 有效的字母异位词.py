import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = collections.defaultdict(int)
        for s_s in s:
            dic[s_s] += 1
        for s_t in t:
            dic[s_t] -= 1
        for val in dic.values():
            if val != 0:
                return False
        return True






class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = collections.defaultdict(int)
        for ss in s:
            counts[ss] += 1
        for tt in t:
            counts[tt] -= 1
        for c in counts.values():
            if c != 0:
                return False
        return True