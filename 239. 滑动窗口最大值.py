import collections
import heapq


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        que = []
        ans = []
        n = len(nums)
        for i in range(k - 1):
            while que and nums[i] >= nums[que[-1]]:
                que.pop()
            que.append(i)

        for i in range(k - 1, n):
            while que and nums[i] >= nums[que[-1]]:
                que.pop()
            que.append(i)
            while que[0] <= i - k:
                que.pop(0)
            ans.append(nums[que[0]])
        return ans



#2
class Solution2:
    def maxSlidingWindow(self, nums, k: int):
        que = collections.deque()
        ans = []
        for i in range(k):
            while que:
                if nums[i] > que[-1]:
                    que.pop()
                else:
                    que.append(nums[i])
                    break
            if not que:
                que.append(nums[i])
        ans.append(que[0])
        for i in range(k, len(nums)):
            if nums[i - k] == que[0]:
                que.popleft()
            while que and nums[i] > que[-1]:
                que.pop()
            que.append(nums[i])
            ans.append(que[0])
        return ans






class Solution3:
    def maxSlidingWindow(self, nums, k: int):
        hp = []
        for i in range(k):
            hp.append(-nums[i])
        heapq.heapify(hp)
        ans = [-hp[0]]
        counts = collections.defaultdict(int)
        for i in range(k, len(nums)):
            counts[nums[i - k]] += 1
            while hp and counts[-hp[0]] > 0:
                counts[-hp[0]] -= 1
                heapq.heappop(hp)
            heapq.heappush(hp, -nums[i])
            ans.append(-hp[0])
        return ans




class Solution4:
    def maxSlidingWindow(self, nums, k: int):
        que = collections.deque()
        ans = []
        for n in nums[:k]:
            while que and n > que[-1]:
                que.pop()
            que.append(n)
        ans.append(que[0])
        for i in range(k, len(nums)):
            while que and nums[i] > que[-1]:
                que.pop()
            que.append(nums[i])
            if nums[i - k] == que[0]:
                que.popleft()
            ans.append(que[0])
        return ans


class Solution5:
    def maxSlidingWindow(self, nums, k: int):
        if k == len(nums):
            return [max(nums)]
        que = collections.deque()
        for i in range(k):
            while que and nums[i] > que[-1]:
                que.pop()
            que.append(nums[i])
        ans = [que[0]]
        for i in range(k, len(nums)):
            if que[0] == nums[i - k]:
                que.popleft()
            while que and nums[i] > que[-1]:
                que.pop()
            que.append(nums[i])
            ans.append(que[0])
        return ans

#nums = [1,3,-1,-3,5,3,6,7]
nums = [2,4,7]
k = 2
s = Solution5()
print(s.maxSlidingWindow(nums, k))