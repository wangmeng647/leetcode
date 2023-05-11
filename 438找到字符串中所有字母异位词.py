class Solution:
    def findAnagrams(self, s: str, p: str):
        counts = [0] * 26
        index = []
        if len(p) > len(s):
            return []
        for i in p:
            counts[ord(i) - 97] -= 1
        for i in range(len(p)):
            counts[ord(s[i]) - 97] += 1
        differ = 0
        for x in counts:
            if x != 0:
                differ += 1
        head = 0
        tail = len(p) - 1
        if differ == 0:
            index.append(head)
        for head in range(1, len(s) - len(p) + 1):
            counts[ord(s[head - 1]) - 97] -= 1
            if counts[ord(s[head - 1]) - 97] == 0:
                differ -= 1
            elif counts[ord(s[head - 1]) - 97] == -1:
                differ += 1
            counts[ord(s[tail + head]) - 97] += 1
            if counts[ord(s[tail + head]) - 97] == 0:
                differ -= 1
            elif counts[ord(s[tail + head]) - 97] == 1:
                differ += 1
            if differ == 0:
                index.append(head)
        return index


s = "bpaa"
p = "aa"
so = Solution()
print(so.findAnagrams(s, p))

