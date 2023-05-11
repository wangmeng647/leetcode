
class Heap:

    def __init__(self):
        self.data = []

    def percolate_down(self, index):
        while index * 2 + 2 <= len(self.data) - 1:
            left = index * 2 + 1
            right = index * 2 + 2
            if self.data[left] > self.data[right]:
                if self.data[left] > self.data[index]:
                    self.data[index], self.data[left] = self.data[left], self.data[index]
                    index = left
                else:
                    break
            else:
                if self.data[right] > self.data[index]:
                    self.data[index], self.data[right] = self.data[right], self.data[index]
                    index = right
                else:
                    break
        if index * 2 + 1 <= len(self.data) - 1:
            if self.data[index] < self.data[-1]:
                self.data[index], self.data[-1] = self.data[-1], self.data[index]

    def percolate_up(self, index):
        father = (index - 1) // 2
        while father >= 0:
            if self.data[father] < self.data[index]:
                self.data[father], self.data[index] = self.data[index], self.data[father]
                index = father
                father = (index - 1) // 2
            else:
                break

    def initial(self, data):
        self.data = data
        for i in reversed(range(len(self.data))):
            self.percolate_down(i)

    def pop(self):
        if not self.data:
            return None
        ans = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self.percolate_down(0)
        return ans

    def insert(self, x):
        self.data.append(x)
        self.percolate_up(len(self.data) - 1)

a = [0,1,2]
h = Heap()
h.insert(3)
h.insert(33)
print(h.data)
