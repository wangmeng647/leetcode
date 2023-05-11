import collections


class Solution:
    def countSmaller(self, nums):
        sort_nums = sorted(set(nums))
        nums.reverse()
        n = len(sort_nums)
        small_sum = [0] * (n + 1)
        ans = []
        num_index = {}
        for i in range(n):
            num_index[sort_nums[i]] = i
        for char in nums:
            index = num_index[char]
            update_index = index + 1
            sum_index = index
            total = 0
            while update_index < (n + 1):
                small_sum[update_index] += 1
                update_index += (-update_index) & update_index

            while sum_index > 0:
                total += small_sum[sum_index]
                sum_index -= (-sum_index) & sum_index
            ans.append(total)
        ans.reverse()
        return ans



#2
class Solution2:
    def countSmaller(self, nums):
        nums.reverse()
        sorted_nums = sorted(set(nums))
        number_index = {}
        smaller_sum = [0] * (len(sorted_nums) + 1)
        ans = []
        for i in range(len(sorted_nums)):
            number_index[sorted_nums[i]] = i
        for n in nums:
            index = number_index[n] + 1
            update_index = index
            sum_index = index - 1
            while update_index < len(smaller_sum):
                smaller_sum[update_index] += 1
                update_index += (-update_index) & update_index
            small_total = 0
            while sum_index > 0:
                small_total += smaller_sum[sum_index]
                sum_index -= (-sum_index) & sum_index
            ans.append(small_total)
        ans.reverse()
        return ans



class Solution3:
    def countSmaller(self, nums):
        re_arrange = sorted(set(nums))
        nums = reversed(nums)
        mp = dict()
        n = len(re_arrange)
        bit = [0] * (n + 1)
        ans = []
        for i in range(n):
            mp[re_arrange[i]] = i + 1
        for digit in nums:
            index = sum_index = mp[digit]
            sum_index -= 1
            total = 0
            while index < n + 1:
                bit[index] += 1
                index += (-index) & index
            while sum_index > 0:
                total += bit[sum_index]
                sum_index ^= (-sum_index) & sum_index
            ans.append(total)
        return list(reversed(ans))




class Solution4:
    def countSmaller(self, nums: list):
        number_idx = dict()
        l = sorted(set(nums))
        nums.reverse()
        ans = []
        for i in range(len(l)):
            number_idx[l[i]] = i + 1
        b_i_t = [0] * (len(l) + 1)

        for n in nums:
            idx_l = idx_r = number_idx[n]
            sum_l = 0
            idx_l -= 1
            while idx_l > 0:
                sum_l += b_i_t[idx_l]
                idx_l ^= idx_l & (-idx_l)
            ans.append(sum_l)
            while idx_r <= len(l):
                b_i_t[idx_r] += 1
                idx_r += idx_r & (-idx_r)
        ans.reverse()
        return ans
s = Solution3()
nums = [1,9,7,8,5]
#nums = [5,2,6,1]
print(s.countSmaller(nums))
