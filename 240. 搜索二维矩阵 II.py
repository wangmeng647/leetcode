
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        def search(nums):
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                if target == nums[mid]:
                    return True
                if target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            if nums[l] == target:
                return True
            else:
                return False
        ans = False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n-1]:
                ans = search(matrix[i])
                if ans is True:
                    return ans
        return ans




#2
class Solution2:
    def searchMatrix(self, matrix, target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                j -= 1
            else:
                i += 1
        return False



class Solution3:
    def searchMatrix(self, matrix, target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            num = matrix[i][j]
            if target == num:
                return True
            if target > num:
                i += 1
            else:
                j -= 1
        return False

s = Solution3()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 52
print(s.searchMatrix(matrix, target))