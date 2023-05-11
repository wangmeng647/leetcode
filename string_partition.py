

def partition(s: str):
    ans = []
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            ans.append(s[i:j + 1])
    return ans

def partition2(s: str):
    n = len(s)
    ans = []
    combination = []

    def dfs(index1, index2):
        if index2 == n - 1:
            combination.append(s[index1: index2 + 1])
            ans.append(combination[:])
            combination.pop()
            return
        combination.append(s[index1:index2 + 1])
        dfs(index2 + 1, index2 + 1)
        combination.pop()
        dfs(index1, index2 + 1)

    dfs(0, 0)
    return ans
