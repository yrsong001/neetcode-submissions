class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        total = 0
        start = 0
        for i in range(len(gas)):
            # while total >= 0:
            total += (gas[i] - cost[i]) # we need to use ()!!
            if total < 0:
                total = 0
                start = i + 1 # bc we only have one start point.
        return start