class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        INFINITY = 2147483647

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r, c, 0])

        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        while queue:
            r, c, steps = queue.popleft()
            for dr, dc in directions:
                x, y = r + dr, c + dc
                if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == INFINITY:
                    grid[x][y] = steps + 1
                    queue.append([x, y, steps + 1])