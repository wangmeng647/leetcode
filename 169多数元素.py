
class Solution:
    def majorityElement(self, nums) -> int:
        count =  1
        majority = nums[0]
        for num in nums[1:]:
            if count == 0:
                majority = num
                count += 1
            else:
                if majority == num:
                    count += 1
                else:
                    count -= 1
        return majority
nums = [6,6,6,7,7]
s = Solution()
print(s.majorityElement(nums))

#2
class Solution1:
    def majorityElement(self, nums) -> int:
        counts = 1
        maj = nums[0]
        for n in nums[1:]:
            if counts == 0:
                maj = n
                counts += 1
            else:
                if maj == n:
                    counts += 1
                else:
                    counts -= 1
        return maj
nums = [10,9,9,9,10]
s = Solution1()
print(s.majorityElement(nums))