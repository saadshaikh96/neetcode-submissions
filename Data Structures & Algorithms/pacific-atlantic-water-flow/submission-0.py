class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        flowsIntoPacific = set()
        flowsIntoAtlantic = set()

        pacificBorder = deque()
        atlanticBorder = deque()
        for c in range(COLS):
            pacificBorder.append([0, c])
            atlanticBorder.append([ROWS - 1, c])

        for r in range(ROWS):
            pacificBorder.append([r, 0])
            atlanticBorder.append([r, COLS - 1])

        self.bfs(pacificBorder, flowsIntoPacific, heights)
        self.bfs(atlanticBorder, flowsIntoAtlantic, heights)

        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in flowsIntoPacific and (r,c) in flowsIntoAtlantic:
                    result.append([r,c])

        return result

    def bfs(self, queue, flowsIntoOcean, heights):
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            r, c = queue.popleft()
            flowsIntoOcean.add((r,c))
            for dr, dc in directions:
                x, y = r + dr, c + dc
                if 0 <= x < ROWS and 0 <= y < COLS and (x,y) not in flowsIntoOcean and heights[x][y] >= heights[r][c]:
                    queue.append([x, y])