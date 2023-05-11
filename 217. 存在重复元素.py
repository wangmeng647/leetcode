
class Solution:
    def containsDuplicate(self, nums) -> bool:
        check = set()
        for n in nums:
            if n in check:
                return True
            check.add(n)
        return False