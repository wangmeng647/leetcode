import random


#快速排序
def quick_select_sort(nums, l, r):
    if l >= r:
        return
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
    quick_select_sort(nums, begin, l - 1)
    quick_select_sort(nums, l + 1, end)

#归并排序
def sort(l, r):
    if l == r:
        return [nums[l]]
    mid = (l + r) // 2
    l1 = sort(l, mid)
    l2 = sort(mid + 1, r)
    result = []
    while l1 and l2:
        if l1[0] > l2[0]:
            result.append(l2[0])
            l2.pop(0)
        else:
            result.append(l1[0])
            l1.pop(0)
    if l1:
        return result + l1
    else:
        return result + l2

nums = [1,5,3,6,2,4,5,4,2,3]
n = len(nums)
#random.shuffle(nums)
print(sort(0, n - 1))


