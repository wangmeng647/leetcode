import heapq
import collections

class Solution:
    def topKFrequent(self, nums, k: int):
        dic = collections.defaultdict(int)
        dic2 = collections.defaultdict(list)
        for word in nums:
            dic[word] += 1
        h = []
        for key, value in dic.items():
            dic2[value].append(key)
            h.append(-value)
        heapq.heapify(h)
        ans = []
        for _ in range(k):
            ans.append(dic2[-heapq.heappop(h)].pop())
        return ans





#2
class Solution2:
    def topKFrequent(self, nums, k: int):
        dic = collections.defaultdict(int)
        dic2 = collections.defaultdict(list)
        for word in nums:
            dic[word] += 1
        h = []
        for key, value in dic.items():
            dic2[value].append(key)
            h.append(-value)
        heapq.heapify(h)
        ans = []
        for _ in range(k):
            ans.append(dic2[-heapq.heappop(h)].pop())
        return ans


s = Solution()
nums = [1,2]
k = 2
print(s.topKFrequent(nums, k))