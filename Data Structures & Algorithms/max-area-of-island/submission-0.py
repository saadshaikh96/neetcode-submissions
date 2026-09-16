class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def explore(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return 0

            if grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            return 1 + explore(row + 1, col) + explore(row - 1, col) + explore(row, col + 1) + explore(row, col - 1)

        maxArea = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    area = explore(row, col)
                    maxArea = max(maxArea, area)

        return maxArea
