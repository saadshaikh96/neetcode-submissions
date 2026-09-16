class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def explore(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            explore(row + 1, col)
            explore(row - 1, col)
            explore(row, col + 1)
            explore(row, col - 1)
            
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    islands += 1
                    explore(row, col)

        return islands
        