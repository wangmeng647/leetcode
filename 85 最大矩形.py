class Solution:
    def maximalRectangle(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        left_ones = [[0] * n for _ in range(m)]
        for i in range(m):
            left_ones[i][0] = int(matrix[i][0])
        for i in range(m):
            for j in range(1, n):
                left_ones[i][j] = (left_ones[i][j - 1] + 1) if matrix[i][j] == '1' else 0
        for j in range(n):
            stack = []
            left_bound = [0] * m
            right_bound = [0] * m
            for i in range(m):
                while stack and left_ones[stack[-1]][j] >= left_ones[i][j]:
                    index = stack.pop()
                    right_bound[index] = i
                left_bound[i] = stack[-1] if stack else -1
                stack.append(i)
            while stack:
                index = stack.pop()
                right_bound[index] = m
            max_i = max(left_ones[i][j] * (right_bound[i] - left_bound[i] - 1) for i in range(m))
            max_area = max(max_area, max_i)
        return max_area

s = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

print(s.maximalRectangle(matrix))
