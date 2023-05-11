class Solution:
    def longestConsecutive(self, nums) -> int:
        sets = set(nums)
        max_len = 0
        for num in sets:
            if num - 1 not in sets:
                cur_num = num
                cur_len = 1
                while cur_num + 1 in sets:
                    cur_num += 1
                    cur_len += 1
                max_len = max(max_len, cur_len)
        return max_len




#2
class Solution2:
    def longestConsecutive(self, nums) -> int:
        un_visited = set(nums)
        visited = {}
        max_l = 0
        while un_visited:
            pre = start = un_visited.pop()
            counts = 1
            while start + 1 in un_visited:
                counts += 1
                start += 1
                un_visited.remove(start)
            if start + 1 in visited:
                counts += visited[start + 1]
            visited[pre] = counts
            max_l = max(max_l, counts)
        return max_l


#3
class Solution3:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        n_set = set(nums)
        max_len = 1
        for n in n_set:
            if n - 1 not in n_set:
                c = 1
                while n + 1 in n_set:
                    c += 1
                    n += 1
                max_len = max(max_len, c)
        return max_len
nums = [1,0,-1]
s = Solution2()
print(s.longestConsecutive(nums))