class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        assert len(gas) == len(cost)
        tank = 0
        lowest = 0
        lowest_index = 0
        for k in range(len(gas)):
            tank = tank + gas[k] - cost[k]
            if tank < lowest:
                lowest_index = k + 1
                lowest = tank

        tank = 0
        for i in chain(range(lowest_index, len(gas)), range(lowest_index)):
            tank += gas[i] - cost[i]
            if tank < 0:
                return -1

        return lowest_index