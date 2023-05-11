import collections


class Solution:
    def intersect(self, nums1, nums2):
        dic = collections.defaultdict(int)
        ans = []
        for n1 in nums1:
            dic[n1] += 1
        for n2 in nums2:
            dic[n2] -= 1
            if dic[n2] >= 0:
                ans.append(n2)
        return ans