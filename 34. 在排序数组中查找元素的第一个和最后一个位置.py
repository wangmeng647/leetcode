
class Solution:
    def searchRange(self, nums, target: int):
        while not nums:
            return [-1, -1]
        k = 0
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                k = mid
                break
            if target < nums[mid]:
                r = mid - 1
                if r == l:
                    k = r
                    break
            else:
                l = mid + 1
                if r == l:
                    k = r
                    break
        if nums[k] != target:
            return [-1, -1]
        index1 = index2 = k
        while 0 <= index1 and nums[index1] == target:
                index1 -= 1

        while index2 <= len(nums) - 1 and nums[index2] == target:
                index2 += 1
        if index2 - index1 == 2:
            return [index1 + 1, index1 + 1]
        else:
            return [index1 + 1, index2 - 1]
'''nums = [1,2,2,2,3,4,5]
target = 2
s = Solution()
print(s.searchRange(nums, target))'''


#2
class Solution1:
    def searchRange(self, nums, target: int):
        if not nums:
            return [-1, -1]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        index1 = l

        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        index2 = l
        if nums[index1] == target:
            return [index1, index2 - 1]
        else:
            return [-1, -1]



class Solution2:
    def searchRange(self, nums, target: int):
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if target <= nums[mid]:
                r = mid
            else:
                l = mid + 1
        start = l
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        if nums[start] != target:
            return [-1, -1]
        return [start, l - 1]
nums = [1]
target = 1
s = Solution2()
print(s.searchRange(nums, target))