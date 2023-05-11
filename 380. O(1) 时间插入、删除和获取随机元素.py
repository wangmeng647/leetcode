import collections
import random


class RandomizedSet:

    def __init__(self):
        self.data = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        else:
            self.data.append(val)
            self.dic[val] = len(self.data) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        index = self.dic[val]

        if index == len(self.data) - 1:
            self.data.pop()
        else:
            self.data[index] = self.data.pop()
            self.dic[self.data[index]] = index
        del self.dic[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)

#["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
#[[],[0],[1],[0],[2],[1],[]]
r = RandomizedSet()
r.insert(0)
r.insert(1)
r.remove(0)
r.insert(2)
r.remove(1)
r.getRandom()


#2
class RandomizedSet2:
    def __init__(self):
        self.dic = {}
        self.data = []
    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        else:
            self.dic[val] = len(self.data)
            self.data.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        else:
            if self.dic[val] == len(self.data) - 1:
                self.data.pop()
            else:
                cache = self.data.pop()
                self.data[self.dic[val]] = cache
                self.dic[cache] = self.dic[val]
            self.dic.pop(val)
            return True
    def getRandom(self) -> int:
        return random.choice(self.data)