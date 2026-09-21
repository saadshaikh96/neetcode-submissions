class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minWays = [float("inf")] * (amount + 1)
        minWays[0] = 0
        for coin in coins:
            for i in range(1, amount + 1):
                if i - coin >= 0:
                    minWays[i] = min(minWays[i], minWays[i - coin] + 1)

        return -1 if minWays[-1] == float("inf") else minWays[-1]