
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        index1 = m - 1
        index2 = n - 1
        for i in reversed(range(len(nums1))):
            if index2 >= 0 and index1 >= 0:
                if nums2 and nums2[index2] >= nums1[index1]:
                    nums1[i] = nums2[index2]
                    index2 -= 1
                else:
                    nums1[i] = nums1[index1]
                    index1 -= 1
            elif index1 < 0:
                nums1[i] = nums2[index2]
                index2 -= 1
            elif index2 < 0:
                return nums1
        return nums1






nums1 = [2,0]
m = 1
nums2 = [1]
n = 1
s = Solution()
print(s.merge(nums1, m, nums2, n))


class Solution1:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        index1 = m - 1
        index2 = n - 1
        for i in reversed(range(m + n)):
            if index2 >= 0 and index1 >= 0:
                if nums1[index1] > nums2[index2]:
                    nums1[i] = nums1[index1]
                    index1 -= 1
                else:
                    nums1[i] = nums2[index2]
                    index2 -= 1
            elif index1 < 0:
                nums1[i] = nums2[index2]
                index2 -= 1
            else:
                return nums1
        return nums1

