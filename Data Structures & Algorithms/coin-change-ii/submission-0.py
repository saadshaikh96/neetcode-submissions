class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        numWays = [0 for a in range(amount + 1)]
        numWays[0] = 1

        for coin in coins:
            for amt in range(coin, amount + 1):
                numWays[amt] += numWays[amt - coin]

        return numWays[-1]