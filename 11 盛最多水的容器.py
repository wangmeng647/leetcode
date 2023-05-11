
class Solution:
    def maxArea(self, height) -> int:
        max_water = 0
        l = 0
        r = len(height) - 1
        while l != r:
            max_water = max(min(height[l], height[r]) * (r - l), max_water)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water



#2
class Solution1:
    def maxArea(self, height) -> int:
        max_area = 0
        n = len(height)
        l, r = 0, n - 1
        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


class Solution2:
    def maxArea(self, height) -> int:
        l, r = 0, len(height) - 1
        mx = 0
        while l < r:
            mx = max(mx, min(height[l], height[r]) * (r - l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return mx

s = Solution2()
height = [1,8,6,2,5,4,8,3,7]
print(s.maxArea(height))