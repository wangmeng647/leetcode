import collections
from collections import defaultdict

class Solution:
    def findWords(self, board, words):
        class Trie:
            def __init__(self):
                self.tree = [0] * 26
                self.end = False
        def create_trie(word, trie):
            for char in word:
                index = ord(char) - 97
                if trie.tree[index]:
                    trie = trie.tree[index]
                else:
                    trie.tree[index] = Trie()
                    trie = trie.tree[index]
            return trie

        def dfs(i, j, t):
            visited.add((i, j))
            combine.append(board[i][j])
            if t.end:
                ans.add(''.join(combine))
            for step_i, step_j in move:
                nx_i, nx_j = i + step_i, j + step_j
                if 0 <= nx_i < m and 0 <= nx_j < n and (nx_i, nx_j) not in visited:
                    nx_trie = t.tree[ord(board[nx_i][nx_j]) - 97]
                    if nx_trie:
                        dfs(nx_i, nx_j, nx_trie)
                        if not any(nx_trie.tree):
                            t.tree[ord(board[nx_i][nx_j]) - 97] = 0

            visited.discard((i, j))
            combine.pop()

        head = Trie()
        for w in words:
            trie = head
            create_trie(w, trie).end = True
        ans = set()
        combine = []
        m, n = len(board), len(board[0])
        move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        for i in range(m):
            for j in range(n):
                if head.tree[ord(board[i][j]) - 97]:
                    dfs(i, j, head.tree[ord(board[i][j]) - 97])

        return list(ans)




#leetcodeofficial


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word


class Solution2:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(now, i1, j1):
            if board[i1][j1] not in now.children:
                return

            ch = board[i1][j1]

            nxt = now.children[ch]
            if nxt.word != "":
                ans.append(nxt.word)
                nxt.word = ""

            if nxt.children:
                board[i1][j1] = "#"
                for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
                    if 0 <= i2 < m and 0 <= j2 < n:
                        dfs(nxt, i2, j2)
                board[i1][j1] = ch

            if not nxt.children:
                now.children.pop(ch)

        ans = []
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        return ans




#
class Solution3:
    def findWords(self, board, words):
        class Trie:
            def __init__(self):
                self.tree = collections.defaultdict(Trie)
                self.end = False

        def create_trie(word, trie):
            for char in word:
                index = ord(char) - 97
                if index in trie.tree:
                    trie = trie.tree[index]
                else:
                    trie.tree[index] = Trie()
                    trie = trie.tree[index]
            return trie

        def dfs(i, j, t):
            if (i, j) in visited:
                return
            visited.add((i, j))
            combine.append(board[i][j])
            if t.end:
                ans.add(''.join(combine))
            for step_i, step_j in move:
                nx_i, nx_j = i + step_i, j + step_j
                if 0 <= nx_i < m and 0 <= nx_j < n and (ord(board[nx_i][nx_j]) - 97) in t.tree:
                    dfs(nx_i, nx_j, t.tree[ord(board[nx_i][nx_j]) - 97])
            visited.discard((i, j))
            combine.pop()

        head = Trie()
        for w in words:
            trie = head
            create_trie(w, trie).end = True
        ans = set()
        combine = []
        m, n = len(board), len(board[0])
        move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        for i in range(m):
            for j in range(n):
                if (ord(board[i][j]) - 97) in head.tree:
                    head_nx = head.tree[ord(board[i][j]) - 97]
                    dfs(i, j, head_nx)

        return list(ans)

s = Solution()
board = [["a","b"],["a","a"]]
words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
r = s.findWords(board, words)
print(r)