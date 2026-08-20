class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)

        if sum(gas) < sum(cost):
            return -1

        start = 0
        total = 0
        for i in range(length):
            total += gas[i]-cost[i]
            if total < 0:
                total = 0
                start = i + 1
        return start


        