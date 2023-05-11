import collections

class Solution:
    def leastInterval(self, tasks, n: int):
        counter_map = collections.Counter(tasks)
        couter_list = []
        max_count = 0
        total_count = 0
        for value in counter_map.values():
            total_count += value
            if value > max_count:
                couter_list.clear()
                couter_list.append(value)
                max_count = value
            elif value == max_count:
                couter_list.append(value)
        least_matrix_count = max_count * (n + 1)
        n_max_count = len(couter_list)
        rest = total_count - n_max_count * max_count
        #if total_count >= least_matrix_count:
            #return total_count
        if rest >= (n + 1 - n_max_count) * (max_count - 1):
            return total_count
        else:
            return least_matrix_count - (n + 1 - n_max_count)




tasks = ["A","B","C","D","A","B","V"]
n = 3
s  = Solution()
print(s.leastInterval(tasks,n))