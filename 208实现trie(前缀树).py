
class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.end = False
    def searchPrefix(self, word):
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if node.children[ch] is None:
                return None
            node = node.children[ch]
        return node
    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.end = True
    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.end
    def startwith(self, word):
        return self.searchPrefix(word) is not None
T = Trie()
t = T.insert('qwe')
print(t)




class Trie1:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

    def search(self, word):
        node = self.searchprefix(word)
        if node:
            return node.end
        else:
            return False
    def insert(self, word):
        node = self
        for char in word:
            index = ord(char) - 97
            if node.children[index] is None:
                node.children[index] = Trie()
            node = node.children[index]
        node.end = True

    def startWith(self, prefix):
        return self.searchprefix(prefix) is not None


    def searchprefix(self, pre):
        node = self
        for char in pre:
            index = ord(char) - 97
            if node.children[index] is None:
                return None
            node = node.children[index]

        return node


#2
class Trie:
    def __init__(self):
        self.dic = [0] * 26
        self.end = False

    def insert(self, word):
        node = self
        for char in word:
            if node.dic[ord(char) - 97]:
                node = node.dic[ord(char) - 97]
            else:
                node.dic[ord(char) - 97] = Trie()
                node = node.dic[ord(char) - 97]
        node.end = True
    def search(self, word):
        node = self
        for char in word:
            if node.dic[ord(char) - 97]:
                node = node.dic[ord(char) - 97]
            else:
                return False
        if node.end:
            return True
        return False

    def startsWith(self, prefix):
        node = self
        for char in prefix:
            if node.dic[ord(char) - 97]:
                node = node.dic[ord(char) - 97]
            else:
                return False
        return True

