
class Solution:
    def trap(self, height) -> int:
        n = len(height)
        left_max = [height[0]] + [0] * (n - 1)
        right_max = [0] * (n - 1) + [height[n - 1]]
        total = 0
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        for i in reversed(range(n - 1)):
            right_max[i] = max(right_max[i + 1], height[i])
        for i in range(n):
            total += min(left_max[i], right_max[i]) - height[i]
        return total


class Solution2:
    def trap(self, height) -> int:
        n = len(height)
        total = 0
        left_max = height[0]
        right_max = height[n - 1]
        left_index = 0
        right_index = n - 1
        while left_index < right_index:
            if left_max < right_max:
                total += left_max - height[left_index]
                left_index += 1
                left_max = max(left_max, height[left_index])
            else:
                total += right_max - height[right_index]
                right_index -= 1
                right_max = max(right_max, height[right_index])
        return total


class Solution3:
    def trap(self, height) -> int:
        ans = 0
        stack = list()
        n = len(height)

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)

        return ans

class Solution4:
    def trap(self, height) -> int:
        n = len(height)
        height_l, height_r = [0], [0]
        z = 0
        for h in height[:n - 1]:
            if h > z:
                z = h
            height_l.append(z)
        z = 0
        height.reverse()
        for h in height[:n - 1]:
            if h > z:
                z = h
            height_r.append(z)
        height_r.reverse()
        height.reverse()
        total = 0
        for i in range(n):
            h_min = min(height_l[i], height_r[i])
            if h_min > height[i]:
                total += h_min - height[i]
        return total

class Solution5:
    def trap(self, height) -> int:
        n = len(height)
        index_l, index_r = 0, n - 1
        l_max, r_max = 0, 0
        total = 0
        while index_l <= index_r:
            if l_max <= r_max:
                if height[index_l] <= l_max:
                    total += l_max - height[index_l]
                else:
                    l_max = height[index_l]
                index_l += 1
            else:
                if height[index_r] <= r_max:
                    total += r_max - height[index_r]
                else:
                    r_max = height[index_r]
                index_r -= 1
        return total

class Solution6:
    def trap(self, height) -> int:
        l_max, r_max = height[0], height[-1]
        l, r = 1, len(height) - 2
        total = 0
        while l <= r:
            if l_max < r_max:
                if l_max > height[l]:
                    total += l_max - height[l]
                l_max = max(l_max, height[l])
                l += 1
            else:
                if height[r] < r_max:
                    total += r_max - height[r]
                r_max = max(r_max, height[r])
                r -= 1
        return total


height = [0,1,0,2,1,0,1,3,2,1,2,1]
#height = [4,2,0,3,2,5]
s = Solution6()
print(s.trap(height))
