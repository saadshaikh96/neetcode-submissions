class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        heap = [(grid[0][0], 0, 0)]

        min_time = 0
        while heap:
            elevation, row, col = heapq.heappop(heap)
            if (row, col) in visited:
                continue
            visited.add((row, col))
            min_time = max(min_time, elevation)
            if row == n - 1 and col == n - 1:
                return min_time
            
            for next_row, next_col in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= next_row < n and 0 <= next_col < n and (next_row, next_col) not in visited:
                    heapq.heappush(heap, (grid[next_row][next_col], next_row, next_col))
