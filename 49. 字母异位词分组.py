import collections


class Solution:
    def groupAnagrams(self, strs):
        mp = collections.defaultdict(list)
        for word in strs:
            num = [0]*26
            for letter in word:
                num[ord(letter) - 97] += 1
            key = tuple(num)
            mp[key].append(word)
        return list(mp.values())


#2
class Solution1:
    def groupAnagrams(self, strs):
        dic = collections.defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for ss in s:
                counts[ord(ss) - 97] += 1
            dic[tuple(counts)].append(s)
        return list(dic.values())


class Solution2:
    def groupAnagrams(self, strs):
        dic = collections.defaultdict(list)
        for sub in strs:
            count = [0] * 26
            for char in sub:
                count[ord(char) - 97] += 1
            dic[tuple(count)].append(sub)
        ans = []
        for i in dic.values():
            ans.append(i)
        return ans