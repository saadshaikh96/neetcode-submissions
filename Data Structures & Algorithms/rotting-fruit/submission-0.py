class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        numFresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    numFresh += 1
                elif grid[i][j] == 2:
                    queue.append([i, j])

        minutes = 0
        while queue and numFresh > 0:
            queueSize = len(queue)
            for _ in range(queueSize):
                i, j = queue.popleft()
                for x,y in self.getNeighbors(i, j, grid):
                    if grid[x][y] == 1:
                        grid[x][y] = 2
                        numFresh -= 1
                        queue.append([x, y])
            minutes += 1

        return minutes if numFresh == 0 else -1
        
    def getNeighbors(self, r, c, grid):
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = []
        if r > 0:
            neighbors.append([r-1, c])
        if r < ROWS - 1:
            neighbors.append([r + 1, c])
        if c > 0:
            neighbors.append([r, c - 1])
        if c < COLS - 1:
            neighbors.append([r, c + 1])
        return neighbors