
class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        gas_remain = 0
        start = index = 0
        n = len(gas)
        steps = 0
        while start < n:
            while steps < n:
                gas_remain += gas[index]
                gas_remain -= cost[index]
                if index < n - 1:
                    index += 1
                else:
                    index = 0
                if gas_remain >= 0:
                    steps += 1
                else:
                    gas_remain = 0
                    steps = 0
                    break
            if steps == n:
                return start
            if start < index:
                start = index
            else:
                return -1





#2
class Solution2:
    def canCompleteCircuit(self, gas, cost) -> int:
        n = len(gas)
        start = 0
        cir = False
        while start < n and not cir:
            remain = gas[start]
            begin = start
            steps = 0
            while remain - cost[start] >= 0:

                remain -= cost[start]
                steps += 1
                if steps == n:
                    return begin
                if start == n - 1:
                    cir = True
                    start = 0
                else:
                    start += 1
                remain += gas[start]
            start += 1
        return -1

gas = [3,3,4]
cost = [3,4,4]
s = Solution2()
print(s.canCompleteCircuit(gas, cost))