class NestedIterator:
    def nest(self, l):
        for sub_l in l:
            if isinstance(sub_l, int):
                self.ans.append(sub_l)
            else:
                self.nest(sub_l)
    def __init__(self, nestedList):
        self.ans = []
        self.nest(nestedList)
    def next(self) -> int:
        return self.ans.pop(0)
    def hasNext(self) -> bool:
        if self.ans:
            return True
        else:
            return False

class NestedIterator1:
    def __init__(self, nestedList):
        self.nestedlist = nestedList
        self.iterator = self.nested(self.nestedlist)
    def next(self) -> int:
        return self.val
    def hasNext(self) -> bool:
        try:
            self.val = next(self.iterator)
            return True
        except:
            return False
    def nested(self, l):
        for sub_l in l:
            if isinstance(sub_l, int):
                yield sub_l
            else:
                yield from self.nested(sub_l)

class NestedIterator_leetcode(object):
    def __init__(self, nestedList):
        self.nestedlist = nestedList
        self.iterator = self.nested(self.nestedlist)
    def next(self) -> int:
        return self.val
    def hasNext(self) -> bool:
        try:
            self.val = next(self.iterator)
            return True
        except:
            return False
    def nested(self, l):
        for sub_l in l:
            if sub_l.isInteger():
                yield sub_l.getInteger()
            else:
                yield from self.nested(sub_l.getList())




#2
class NestedIterator2:
    def __init__(self, nestedList):
        self.iter = self.iterator(nestedList)
    def next(self) -> int:
        return self.val
    def hasNext(self) -> bool:
        try:
            self.val = next(self.iter)
            return True
        except:
            return False

    def iterator(self, ls):
        for i in ls:
            if isinstance(i, int):
                yield i
            else:
                yield from self.iterator(i)



class NestedIterator3:
    def __init__(self, nestedList):
        self.iterator = self.iter(nestedList)

    def hasNext(self):
        try:
            self.val = next(self.iterator)
            return True
        except:
            return False

    def next(self):
        return self.val

    def iter(self, ls):
        for n in ls:
            if isinstance(n, int):
                yield n
            else:
                yield from self.iter(n)
nestedList = [[1,[3,4]],2,[1,1]]
s = NestedIterator3(nestedList)
while s.hasNext():
    print(s.next())
print(s.iter)