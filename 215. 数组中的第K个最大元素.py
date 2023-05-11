

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        def quick_select_sort(nums, l, r, k):
            if l >= r:
                return nums[l]
            begin = l
            end = r
            selected = nums[l]
            while l < r:
                while l < r:
                    if selected < nums[r]:
                        r -= 1
                    else:
                        nums[l] = nums[r]
                        l += 1
                        break
                while l < r:
                    if nums[l] < selected:
                        l += 1
                    else:
                        nums[r] = nums[l]
                        r -= 1
                        break
            nums[l] = selected
            if l == len(nums) - k:
                return nums[l]
            elif l > len(nums) - k:
                num = quick_select_sort(nums, begin, l - 1, k)
            else:
                num = quick_select_sort(nums, l + 1, end, k)
            return num
        return quick_select_sort(nums, 0, len(nums) - 1, k)




#2
class Solution2:
    def findKthLargest(self, nums, k: int) -> int:
        start, end = 0, len(nums) - 1
        k = len(nums) - k
        while True:
            l, r = start, end
            select_num = nums[start]
            if l == r:
                return select_num
            while True:
                while True:
                    if l == r:
                        break
                    if select_num < nums[r]:
                        r -= 1
                    else:
                        nums[l] = nums[r]
                        l += 1
                        break
                while True:
                    if l == r:
                        break
                    if select_num > nums[l]:
                        l += 1
                    else:
                        nums[r] = nums[l]
                        r -= 1
                        break
                if l == r:
                    if l == k:
                        return select_num
                    elif l > k:
                        end = l - 1
                        break
                    else:
                        start = l + 1
                        break




class Solution3:
    def findKthLargest(self, nums, k: int) -> int:
        pivot = nums[0]
        l, r, n = 0, len(nums) - 1, len(nums)
        begin, end = l, r
        k = n - k
        while True:
            while l < r and pivot < nums[r]:
                r -= 1
            nums[l] = nums[r]
            if l == r:
                nums[l] = pivot
                if l == k:
                    return nums[l]
                if k < l:
                    end = r = l - 1
                    l = begin
                else:
                    begin = l = l + 1
                    r = end
                if begin == end:
                    if k == begin:
                        return nums[begin]
                    return -1
                pivot = nums[r]
            else:
                l += 1
            while l < r and nums[l] < pivot:
                l += 1
            nums[r] = nums[l]
            if l == r:
                nums[r] = pivot
                if l == k:
                    return nums[l]
                if k < l:
                    end = r = l - 1
                    l = begin
                else:
                    begin = l = l + 1
                    r = end
                if begin == end:
                    if k == begin:
                        return nums[begin]
                    return -1
                pivot = nums[l]
            else:
                r -= 1

s = Solution3()
nums = [3,2,3,1,2,4,5,5,6,5]
k = 1
print(s.findKthLargest(nums, k))

