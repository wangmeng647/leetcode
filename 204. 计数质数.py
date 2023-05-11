from timer import timer

class Solution:
    @timer
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        mark = [1] * n
        for i in range(2, n):
            if mark[i]:
                for j in range(i, n):
                    try:
                        mark[j * i] = 0
                    except:
                        break
        return sum(mark) - 2




class Solution2:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        mark = [1] * n
        primes = []
        for i in range(2, n):
            if mark[i]:
                primes.append(i)
            for p in primes:
                if i * p >= n:
                    break
                mark[p * i] = 0
                if i % p == 0:
                    break
        return len(primes)




#2
class Solution3:
    def countPrimes(self, n: int) -> int:
        mark = [True] * n
        for i in range(2, n):
            if i * i > n - 1:
                break
            if not mark[i]:
                continue
            for j in range(i, n):
                if i * j > n - 1:
                    break
                mark[i * j] = False
        counts = 0
        for i in range(2, n):
            if mark[i]:
                counts += 1
        return counts



class Solution4:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        mark = [1] * n
        mark[0] = mark[1] = 0
        prime = []
        for i in range(2, n):
            if mark[i]:
                prime.append(i)
                for num in prime:
                    if i * num > n - 1:
                        break
                    mark[i * num] = 0
            else:
                for num in prime:
                    if i * num > n - 1:
                        break
                    mark[num * i] = 0
                    if i % num == 0:
                        break
        return len(prime)

s = Solution4()
print(s.countPrimes(10000))