
'''class Solution2:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)
        left, right = [0] * n, [0] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans'''










class Solution:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)
        left_bound = [0] * n
        right_bound = [n] * n
        stack = list()
        for i in range(0, n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            left_bound[i] = stack[-1] if stack else -1
            stack.append(i)
        stack2 = []
        for i in reversed(range(0, n)):
            while stack2 and heights[i] <= heights[stack2[-1]]:
                stack2.pop()
            right_bound[i] = stack2[-1] if stack2 else n
            stack2.append(i)
        aera = [0] * n
        for i in range(n):
            aera[i] = (right_bound[i] - left_bound[i] - 1) * heights[i]
        return max(aera) if n > 0 else 0


class Solution3:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)
        left_bound = [0] * n
        right_bound = [0] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                index = stack.pop()
                right_bound[index] = i
            left_bound[i] = stack[-1] if stack else -1
            stack.append(i)
        while stack:
            index = stack.pop()
            right_bound[index] = n
        return max(heights[i] * (right_bound[i] - left_bound[i] - 1) for i in range(n))






#2
class Solution4:
    def largestRectangleArea(self, heights) -> int:
        area = 0
        n = len(heights)
        mono_stack = []
        l_boarder, r_boarder = [], []
        for i in range(n):
            while mono_stack and heights[i] <= heights[mono_stack[-1]]:
                mono_stack.pop()
            if mono_stack:
                l_boarder.append(mono_stack[-1])
            else:
                l_boarder.append(-1)
            mono_stack.append(i)
        mono_stack.clear()
        for i in reversed(range(n)):
            while mono_stack and heights[i] <= heights[mono_stack[-1]]:
                mono_stack.pop()
            if mono_stack:
                r_boarder.append(mono_stack[-1])
            else:
                r_boarder.append(n)
            mono_stack.append(i)
        r_boarder.reverse()
        for i in range(n):
            area = max(heights[i] * (r_boarder[i] - l_boarder[i] - 1), area)
        return area




class Solution5:
    def largestRectangleArea(self, heights) -> int:
        heights_l, heights_r = [], []
        n = len(heights)
        stack = []
        for i in range(n):
            while stack:
                index = stack[-1]
                if heights[index] < heights[i]:
                    heights_l.append(index)
                    stack.append(i)
                    break
                stack.pop()
            if not stack:
                stack.append(i)
                heights_l.append(-1)
        stack.clear()
        for i in reversed(range(n)):
            while stack:
                index = stack[-1]
                if heights[index] < heights[i]:
                    heights_r.append(index)
                    stack.append(i)
                    break
                stack.pop()
            if not stack:
                stack.append(i)
                heights_r.append(n)
        heights_r.reverse()
        mx = 0
        for i in range(n):
            mx = max(mx, heights[i] * (heights_r[i] - heights_l[i] - 1))
        return mx



#heights = [6,7,5,2,4,5,9,3]
heights = [2,1,5,6,2,3]
s = Solution5()
print(s.largestRectangleArea(heights))