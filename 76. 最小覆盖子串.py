
'''class Solution:
    def minWindow(self, s, t):
        min_len = len(s) + 1
        head_str = ''
        min_str = ''
        tail = 0
        head = 0
        letters_counts = {}
        for le in t:
            if le not in letters_counts:
                letters_counts[le] = -1
            else:
                letters_counts[le] -= 1
        differ = len(letters_counts)
        for head_i in range(len(s)):
            if s[head_i] in letters_counts:
                head_str = s[head_i]
                head = head_i
                tail = head_i
                letters_counts[head_str] += 1
                if letters_counts[head_str] == 0:
                    differ -= 1
                if differ == 0:
                    return head_str
                break
        if head_str == '':
            return head_str
        #while head <= (len(s) - len(t)):
        while True:
            while tail < len(s) - 1:
                tail += 1
                if s[tail] in letters_counts:
                    letters_counts[s[tail]] += 1
                    if letters_counts[s[tail]] == 0:
                        differ -= 1
                        if differ == 0:
                            lenth = tail - head + 1
                            if lenth < min_len:
                                min_len = lenth
                                min_str = s[head:tail + 1]
                            break
                    elif letters_counts[s[tail]] > 0 and letters_counts[s[tail]] == letters_counts[s[head]]:
                        break
            if tail == len(s) - 1:
                break
            letters_counts[s[head]] -= 1
            if letters_counts[s[head]] == -1:
                differ += 1
            while head < tail:
                head += 1
                if s[head] in letters_counts:
                    jdu = letters_counts[s[head]] - 1
                    if jdu < 0:
                        break
                    elif jdu >= 0:
                        letters_counts[s[head]] -= 1
        return min_str'''
import collections


class Solution:
    def minWindow(self, s, t):
        map_counts = {}
        for char in t:
            if char not in map_counts:
                map_counts[char] = -1
            else:
                map_counts[char] -= 1
        differ = len(map_counts)
        min_len = len(s) + 1
        min_str = ''
        head = -1
        tail = 0
        for head_i in range(len(s)):
            if s[head_i] in map_counts:
                head = tail = head_i
                break
        if len(t) > len(s) or head == -1:
            return ''
        while True:
            while tail < len(s):
                if s[tail] in map_counts:
                    map_counts[s[tail]] += 1
                    if map_counts[s[tail]] == 0:
                        differ -= 1
                        if differ == 0:
                            tail += 1
                            break
                tail += 1
                if tail == len(s):
                    return min_str
            while True:
                if s[head] in map_counts:
                    map_counts[s[head]] -= 1
                    if map_counts[s[head]] == -1:
                        differ += 1
                        if tail - head < min_len:
                            min_len = tail - head
                            min_str = s[head:tail]
                        head += 1
                        break
                head += 1
            if tail == len(s):
                return min_str







#2
class Solution2:
    def minWindow(self, s, t):
        counts = collections.defaultdict(int)
        n = len(s)
        ans_l = ans_r = 0
        for char in t:
            counts[char] += 1
        differ = len(counts)
        index_l = index_r = 0
        min_l = n
        while True:
            while index_r < n:
                if s[index_r] in counts:
                    counts[s[index_r]] -= 1
                    if counts[s[index_r]] == 0:
                        differ -= 1
                        if differ == 0:
                            break
                index_r += 1
            if differ != 0:
                break
            while True:
                if s[index_l] in counts:
                    counts[s[index_l]] += 1
                    if counts[s[index_l]] == 1:
                        differ += 1
                        break
                index_l += 1
            if index_r - index_l < min_l:
                min_l = index_r - index_l
                ans_l, ans_r = index_l, index_r
            index_l += 1
            index_r += 1
        if index_l == 0:
            return ''
        return s[ans_l:ans_r + 1]



s = "a"
t = "aa"
solu = Solution2()
print(solu.minWindow(s,t))

