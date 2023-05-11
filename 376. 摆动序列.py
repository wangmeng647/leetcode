
class Solution:
    def wiggleMaxLength(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return n
        len_index = []
        l, r = 0, 1
        while r < n:
            differ = nums[r] - nums[l]
            if differ == 0:
                r += 1
            else:
                if differ > 0:
                    sign = True
                if differ < 0:
                    sign = False
                len_index.append(l)
                break
        if not len_index:
            return 1
        while True:
            while sign and r < n - 1:
                l  = r
                r += 1
                differ = nums[r] - nums[l]
                if differ >= 0:
                    continue
                if differ < 0:
                    len_index.append(l)
                    sign = False
                    break
            while not sign and r < n - 1:
                l = r
                r += 1
                differ = nums[r] - nums[l]
                if differ <= 0:
                    continue
                if differ > 0:
                    len_index.append(l)
                    sign = True
                    break
            if r == n - 1:
                len_index.append(r)
                break
        return len(len_index)
nums = [0,0]
s = Solution()
print(s.wiggleMaxLength(nums))