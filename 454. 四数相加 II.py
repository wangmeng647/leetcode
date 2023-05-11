import collections


class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        set1 = collections.defaultdict(int)
        set2 = collections.defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                set1[n1 + n2] += 1
        for n3 in nums3:
            for n4 in nums4:
                set2[n3 + n4] += 1
        counts = 0
        for half_sum in set1:
            if -half_sum in set2:
                counts += set1[half_sum] * set2[-half_sum]
        return counts





#2
class Solution2:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        dic1 = collections.defaultdict(int)
        counts = 0
        for n1 in nums1:
            for n2 in nums2:
                dic1[n1 + n2] += 1
        for n3 in nums3:
            for n4 in nums4:
                if -(n3 + n4) in dic1:
                    counts += dic1[-(n3 + n4)]
        return counts



class Solution3:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        dic = collections.Counter(a + b for a in nums1 for b in nums2)
        counts = 0
        for a in nums3:
            for b in nums4:
                if -(a + b) in dic:
                    counts += dic[-(a + b)]
        return counts


s = Solution2()
nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
print(s.fourSumCount(nums1, nums2, nums3, nums4))