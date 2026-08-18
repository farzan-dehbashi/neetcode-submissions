class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = dict()
        def calc(i):
            if i in [0,1]:
                return cost[i]

            memo[i] = min(memo[i-1] if i-1 in memo else calc(i-1), memo[i-2] if i-2 in memo else calc(i-2)) + cost[i]
            return memo[i]

        return min(calc(len(cost) - 1), calc(len(cost) - 2))