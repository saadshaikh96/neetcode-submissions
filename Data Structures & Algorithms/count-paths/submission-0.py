class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        numWays = [[1] * (n) for i in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                numWays[row][col] = numWays[row - 1][col] + numWays[row][col - 1]

        return numWays[-1][-1]