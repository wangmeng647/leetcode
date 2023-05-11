
class Solution:
    def reversePairs(self, nums) -> int:
        nums.reverse()
        sort_set = sorted(set(nums))
        n = len(sort_set)
        number_index = {}
        smaller_sum = [0] * (n + 1)
        total = 0
        for i in range(n):
            number_index[sort_set[i]] = i
        for num in nums:
            index = number_index[num] + 1
            small_index = index - 1
            while index < (n + 1):
                smaller_sum[index] += 1
                index += (-index) & index
            while small_index > 0:
                total += smaller_sum[small_index]
                small_index -= (-small_index) & small_index
        return total
s = Solution()
nums = [1,3,2,3,1]
print(s.reversePairs(nums))