import collections
import heapq
# 桶排序
class Solution1:
    def topKFrequent(self, nums, k):
        dic = {}
        dic_count_num = collections.defaultdict(list)
        ans = []
        n = len(nums)
        counts = [None] * (n + 1)
        num_len = [None] * (n + 1)
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        for key, value in dic.items():
            dic_count_num[value].append(key)
        for key, value in dic_count_num.items():
            counts[key] = value
            num_len[key] = len(value)
        z = 0
        for i in range(n, -1, -1):
            if counts[i] is not None:
                ans += counts[i]
                z += num_len[i]
                if z >= k:
                    break
        return ans

# 堆
class Solution2:
    def topKFrequent(self, nums, k):
        counter = collections.Counter
        counter = counter(nums)
        pri_heap = []
        for key, value in counter.items():
            heapq.heappush(pri_heap, (value, key))
            if len(pri_heap) > k:
                heapq.heappop(pri_heap)
        ans = []
        for i in pri_heap:
            ans.append(i[1])
        return ans





nums = [1]
k = 1
s = Solution2()
print(s.topKFrequent(nums, k))

#counter = collections.Counter
#counter = counter(nums)
#for key, value in counter.items():

#nums = [2, 3, 5, 1, 54, 23, 132]
