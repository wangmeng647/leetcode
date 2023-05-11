import collections

#dfs 超时
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList):

        dic_edge = collections.defaultdict(set)
        if beginWord not in set(wordList):
            wordList.insert(0, beginWord)
        n = len(wordList)
        def check(word1, word2):
            c = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    c += 1
            return c
        
        def match(begin):
            if begin == n - 1:
                return
            word = wordList[begin]
            for i in range(begin + 1, n):
                if check(word, wordList[i]) == 1:
                    dic_edge[word].add(wordList[i])
                    dic_edge[wordList[i]].add(word)
            match(begin + 1)
        match(0)
        if endWord not in dic_edge:
            return 0
        min_steps = float('inf')
        
        def dfs(word, steps, word_edge):
            nonlocal min_steps
            if word == endWord:
                min_steps = min(min_steps, steps)
                return
            for del_word in word_edge[word]:
                word_edge[del_word].discard(word)
            for nx_word in word_edge[word]:
                dfs(nx_word, steps + 1, word_edge)
            for del_word in word_edge[word]:
                word_edge[del_word].add(word)

        dfs(beginWord, 1, dic_edge)
        if min_steps == float('inf'):
            return 0
        return min_steps

#single end BFS
class Solution1:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        deque = collections.deque()
        deque.append(beginWord)
        dic_edge = collections.defaultdict(set)
        wordList.append(beginWord)
        searched = set()
        steps = 1
        for word in wordList:
            sub_word = list(word)
            for i in range(len(sub_word)):
                temp = sub_word[i]
                sub_word[i] = '*'
                new_word = ''.join(sub_word)
                dic_edge[word].add(new_word)
                dic_edge[new_word].add(word)
                sub_word[i] = temp
        while deque:
            for _ in range(len(deque)):
                word_search = deque.popleft()
                searched.add(word_search)
                for w in dic_edge[word_search]:
                    if w == endWord:
                        return (steps + 2) // 2
                    if w not in searched:
                        deque.append(w)
            steps += 1
        return 0


#double end BFS
class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        wordList.append(beginWord)
        deque_begin = collections.deque()
        deque_end = collections.deque()
        deque_begin.append(beginWord)
        deque_end.append(endWord)
        dic_edge = collections.defaultdict(set)
        searched_begin = {beginWord}
        searched_end = {endWord}
        steps_begin = 1
        steps_end = 1
        for word in wordList:
            sub_word = list(word)
            for i in range(len(sub_word)):
                temp = sub_word[i]
                sub_word[i] = '*'
                new_word = ''.join(sub_word)
                dic_edge[word].add(new_word)
                dic_edge[new_word].add(word)
                sub_word[i] = temp
        while True:
            n_begin = len(deque_begin)
            for _ in range(n_begin):
                word_search = deque_begin.popleft()
                for w in dic_edge[word_search]:
                    if w in searched_end:
                        return (steps_begin + steps_end + 1) // 2
                    if w not in searched_begin:
                        searched_begin.add(w)
                        deque_begin.append(w)
            steps_begin += 1
            n_end = len(deque_end)
            for _ in range(n_end):
                word_search = deque_end.popleft()
                for w in dic_edge[word_search]:
                    if w in searched_begin:
                        return (steps_end + steps_begin + 1) // 2
                    if w not in searched_end:
                        searched_end.add(w)
                        deque_end.append(w)
            steps_end += 1
            if not deque_begin and not deque_end:
                return 0




#2
class Solution3:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        trans_net = collections.defaultdict(set)
        wordList.append(beginWord)
        n = len(wordList)
        ans = 1
        que1 = collections.deque()
        que2 = collections.deque()
        que1.append(beginWord)
        def match(w1, w2):
            c = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    c += 1
            return True if c == 1 else False

        for i in range(n):
            for j in range(i + 1, n):
                if match(wordList[i], wordList[j]):
                    trans_net[wordList[i]].add(wordList[j])
                    trans_net[wordList[j]].add(wordList[i])

        visited = set()
        while que1 or que2:

            while que1:
                s_word = que1.popleft()
                visited.add(s_word)
                for word in trans_net[s_word]:
                    if word not in visited:
                        visited.add(word)
                        que2.append(word)
            ans += 1
            if endWord in visited:
                return ans
            while que2:
                s_word = que2.popleft()
                visited.add(s_word)
                for word in trans_net[s_word]:
                    if word not in visited:
                        visited.add(word)
                        que1.append(word)
            ans += 1
            if endWord in visited:
                return ans
        return 0

class Solution4:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        trans_net = collections.defaultdict(set)
        wordList.append(beginWord)
        n = len(wordList)
        ans = 1
        que1 = collections.deque()
        que2 = collections.deque()
        que1.append(beginWord)
        for word in wordList:
            l_word = list(word)
            for i in range(len(word)):
                cache = word[i]
                l_word[i] = '*'
                new_word = ''.join(l_word)
                trans_net[word].add(new_word)
                trans_net[new_word].add(word)
                l_word[i] = cache

        visited = set()
        while que1 or que2:

            while que1:
                s_word = que1.popleft()
                visited.add(s_word)
                for word in trans_net[s_word]:
                    if word not in visited:
                        visited.add(word)
                        que2.append(word)
            ans += 1
            if endWord in visited:
                return ans
            while que2:
                s_word = que2.popleft()
                visited.add(s_word)
                for word in trans_net[s_word]:
                    if word not in visited:
                        visited.add(word)
                        que1.append(word)
            ans += 1
            if endWord in visited:
                return ans // 2 + 1
        return 0


class Solution5:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        path = collections.defaultdict(set)
        wordList.append(beginWord)
        for word in wordList:
            ls_word = list(word)
            for i in range(len(ls_word)):
                cache_char = ls_word[i]
                ls_word[i] = '.'
                new_word = ''.join(ls_word)
                path[word].add(new_word)
                path[new_word].add(word)
                ls_word[i] = cache_char
        visited = set()
        visited.add(beginWord)
        stack_1 = [beginWord]
        stack_2 = []
        steps = 1
        found = False
        while stack_1 or stack_2:
            while stack_1:
                word = stack_1.pop()
                for pt in path[word]:
                    if pt == endWord:
                        found = True
                        break
                    if pt not in visited:
                        stack_2.append(pt)
                        visited.add(pt)
            steps += 1
            if found:
                break
            while stack_2:
                word = stack_2.pop()
                for pt in path[word]:
                    if pt == endWord:
                        found = True
                        break
                    if pt not in visited:
                        stack_1.append(pt)
                        visited.add(pt)
            steps += 1
            if found:
                break
        return steps // 2 + 1 if found else 0

s = Solution5()
#beginWord = "lost"
#endWord = "miss"
#wordList = ["most","mist","miss","lost","fist","fish"]
#beginWord = "hit"
#endWord = "cog"
#wordList = ["hot","dot","dog","lot","log","cog"]
beginWord = "qa"
endWord = "sq"
wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]


print(s.ladderLength(beginWord, endWord, wordList))


