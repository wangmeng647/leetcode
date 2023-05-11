

class Solution:
    def search(self, nums, target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        if nums[l] == target:
            return l
        else:
            return -1


'''s = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(s.search(nums, target))'''


#2
class Solution1:
    def search(self, nums, target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if mid == l:
                if nums[mid] == target:
                    return mid
                if nums[r] == target:
                    return r
                return -1
            if nums[mid] == target:
                return mid
            if nums[l] < nums[mid]:
                if nums[l] <= target <= nums[mid - 1]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid + 1] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
s = Solution1()
nums = [1, 2, 3]
target = 2
print(s.search(nums, target))