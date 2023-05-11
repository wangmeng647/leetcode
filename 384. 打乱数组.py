import copy
import random


class Solution:

    def __init__(self, nums):
        self.original = copy.copy(nums)
        self.nums = nums

    def reset(self):
        self.nums = copy.copy(self.original)
        return self.nums

    def shuffle(self):
        shuffle = []
        for i in range(len(self.nums)):
            j = random.randrange(i, len(self.nums))
            shuffle.append(self.nums.pop(j))
        self.nums = shuffle
        return shuffle


class Solution2:

    def __init__(self, nums):
        self.original = copy.copy(nums)
        self.nums = nums

    def reset(self):
        self.nums = copy.copy(self.original)
        return self.nums

    def shuffle(self):
        n = len(self.nums)
        for i in range(n):
            j = random.randrange(i, n)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


#2
class Solution3:

    def __init__(self, nums):
        self.nums = nums
        self.copy = nums[:]
    def reset(self):
        return self.nums

    def shuffle(self):
        n = len(self.nums)
        for i in range(n):
            index = random.randrange(i, n)
            self.copy[i], self.copy[index] = self.copy[index], self.copy[i]
        return self.copy
