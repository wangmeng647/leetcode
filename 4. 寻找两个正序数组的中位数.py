
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            k = l // 2
        else:
            k = l // 2 - 1
        if not nums1:
            if l % 2 == 1:
                return nums2[k]
            else:
                return (nums2[k] + nums2[k + 1]) / 2
        if not nums2:
            if l % 2 == 1:
                return nums1[k]
            else:
                return (nums1[k] + nums1[k + 1]) / 2
        while k != 0:
            if k % 2 == 1:
                index = k // 2
            else:
                index = k // 2 - 1
            if len(nums1) < index + 1:
                if nums1 and nums1[-1] > nums2[index]:
                    nums2 = nums2[index + 1:]
                else:
                    nu1 = nums2[k - len(nums1)]
                    if l % 2 == 0:
                        nu2 = nums2[k - len(nums1) + 1]
                        return (nu1 + nu2) / 2
                    else:
                        return nu1
            elif len(nums2) < index + 1:
                if nums2 and nums2[-1] > nums1[index]:
                    nums1 = nums1[index + 1:]
                else:
                    nu1 = nums1[k - len(nums2)]
                    if l % 2 == 0:
                        nu2 = nums1[k - len(nums2) + 1]
                        return (nu1 + nu2) / 2
                    else:
                        return nu1
            elif nums1[index] >= nums2[index]:
                nums2 = nums2[index + 1:]
            else:
                nums1 = nums1[index + 1:]
            k = k - index - 1
        if l % 2 == 1:
            if nums1 and nums2:
                return min(nums1[0], nums2[0])
            if nums1:
                return nums1[0]
            else:
                return nums2[0]
        else:
            if nums1 and nums2:
                if nums1[0] > nums2[0]:
                    nu1 = nums2[0]
                    nums2.pop(0)
                else:
                    nu1 = nums1[0]
                    nums1.pop(0)
                if nums1 and nums2:
                    nu2 = min(nums1[0], nums2[0])
                    return (nu1 + nu2) / 2
                if nums1:
                    nu2 = nums1[0]
                else:
                    nu2 = nums2[0]
                return (nu1 + nu2) / 2
            if nums1:
                return (nums1[0] + nums1[1]) / 2
            else:
                return (nums2[0] + nums2[1]) / 2




#2
class Solution2:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m, n = len(nums1), len(nums2)
        def search(nums1, nums2, k):
            nums11, nums22 = nums1[:], nums2[:]
            while True:
                if not nums11:
                    return nums22[k - 1]
                if not nums22:
                    return nums11[k - 1]
                if k == 1:
                    return nums11[0] if nums11[0] < nums22[0] else nums22[0]
                elif len(nums11) < k // 2:
                    if nums11[-1] <= nums22[k // 2 - 1]:
                        nums11, k = [], k - len(nums11)
                    else:
                        nums22 = nums22[k // 2:]
                        k = k - k // 2
                elif len(nums22) < k // 2:
                    if nums22[-1] <= nums11[k // 2 - 1]:
                        nums22, k = [], k - len(nums22)
                    else:
                        nums11 = nums11[k // 2:]
                        k = k - k // 2
                elif nums11[k // 2 - 1] < nums22[k // 2 - 1]:
                    nums11 = nums11[k // 2:]
                    k -= k // 2
                else:
                    nums22 = nums22[k // 2:]
                    k -= k // 2
        if (m + n) % 2 == 1:
            k = (m + n) // 2 + 1
            return search(nums1, nums2, k)
        else:
            k = (m + n) // 2
            return (search(nums1, nums2, k) + search(nums1, nums2, k + 1)) / 2

s = Solution2()
nums1 = []
nums2 = [2,3,4,5,6]
print(s.findMedianSortedArrays(nums1, nums2))