import collections
import heapq

class Solution:
    def medianSlidingWindow(self, nums, k):
        if k == 1:
            return nums
        hp_small = []
        hp_large = nums[:k]
        del_counts = collections.defaultdict(int)
        heapq.heapify(hp_large)
        size_s = 0
        size_l = len(hp_large)
        ans = []
        def balance():
            nonlocal size_l, size_s
            while size_s - size_l > 1:
                heapq.heappush(hp_large, -heapq.heappop(hp_small))
                size_s -= 1
                size_l += 1
            while size_l - size_s > 1:
                size_l -= 1
                size_s += 1
                heapq.heappush(hp_small, -heapq.heappop(hp_large))
        balance()
        def median():
            if k % 2 == 0:
                return (-hp_small[0] + hp_large[0]) / 2
            else:
                return -hp_small[0] if size_s > size_l else hp_large[0]
        ans.append(median())
        for i in range(k, len(nums)):
            if nums[i] >= hp_large[0]:
                heapq.heappush(hp_large, nums[i])
                size_l += 1
            else:
                heapq.heappush(hp_small, -nums[i])
                size_s += 1
            del_counts[nums[i - k]] += 1
            if nums[i - k] >= hp_large[0]:
                size_l -= 1
                while hp_large and del_counts[hp_large[0]] > 0 and len(hp_large) > size_l:
                    del_counts[heapq.heappop(hp_large)] -= 1
            else:
                size_s -= 1
                while hp_small and del_counts[-hp_small[0]] > 0 and len(hp_small) > size_s:
                    del_counts[-heapq.heappop(hp_small)] -= 1
            balance()
            while hp_large and del_counts[hp_large[0]] > 0 and len(hp_large) > size_l:
                del_counts[heapq.heappop(hp_large)] -= 1
            while hp_small and del_counts[-hp_small[0]] > 0 and len(hp_small) > size_s:
                del_counts[-heapq.heappop(hp_small)] -= 1
            ans.append(median())
        return ans


from raw_BST_counting import BST
#use bst
class Solution2:
    def medianSlidingWindow(self, nums, k):
        if k == 1:
            return nums
        bst = BST(nums[0])
        ans = []
        def median():
            return bst.search_index(k // 2 + 1) if k % 2 == 1 else (bst.search_index(k // 2 + 1) + bst.search_index(k // 2)) / 2
        for n in nums[1:k]:
            bst.insert(n)
        ans.append(median())
        for i in range(k, len(nums)):
            bst.remove(nums[i - k])
            bst.insert(nums[i])
            ans.append(median())
        return ans




class Solution3:
    def medianSlidingWindow(self, nums, k):
        if k == 1:
            return nums
        small_hp = nums[:k]
        big_hp = []
        heapq.heapify(small_hp)
        delay_cache = collections.defaultdict(int)
        odd = k % 2
        small_size = k
        big_size = 0
        ans = []
        def balance():
            nonlocal small_size, big_size
            while small_size - 1 > big_size:
                heapq.heappush(big_hp, -heapq.heappop(small_hp))
                small_size -= 1
                big_size += 1
            while big_size > small_size:
                heapq.heappush(small_hp, -heapq.heappop(big_hp))
                small_size += 1
                big_size -= 1
        def remove():
            while small_hp and delay_cache[small_hp[0]] > 0:
                delay_cache[small_hp[0]] -= 1
                heapq.heappop(small_hp)
            while big_hp and delay_cache[-big_hp[0]] > 0:
                delay_cache[-big_hp[0]] -= 1
                heapq.heappop(big_hp)
        def add():
            nonlocal small_size, big_size
            if small_hp and nums[i] >= small_hp[0]:
                small_size += 1
                heapq.heappush(small_hp, nums[i])
            else:
                big_size += 1
                heapq.heappush(big_hp, -nums[i])
        def get_mid():
            if odd:
                ans.append(small_hp[0])
            else:
                ans.append((small_hp[0] - big_hp[0]) / 2)
        balance()
        get_mid()
        for i in range(k, len(nums)):
            delay_cache[nums[i - k]] += 1
            if nums[i - k] >= small_hp[0]:
                small_size -= 1
            else:
                big_size -= 1
            remove()
            add()
            balance()
            remove()
            get_mid()
        return ans

s = Solution2()
#nums = [7,0,3,9,9,9,1,7,2,3]
#ans = [2.5,4.0,7.0,7.5,7.5,7.0,7.0]
#wrong = [2.5, 4.0, 7.0, 4.0, 7.0, 7.0, 5.5]
nums = [9,7,0,3,9,8,6,5,7,6]
print(s.medianSlidingWindow(nums, 2))
