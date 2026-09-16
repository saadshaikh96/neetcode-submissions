class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROWS, COLS = len(board), len(board[0])

        def find(row, col, i):
            if i == len(word):
                return True
            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return False
            if (row, col) in visited:
                return False
            if word[i] != board[row][col]:
                return False

            visited.add((row, col))
            found = find(row + 1, col, i + 1) or find(row - 1, col, i + 1) or find(row, col + 1, i + 1) or find(row, col - 1, i + 1)
            visited.remove((row, col))

            return found

        for row in range(ROWS):
            for col in range(COLS):
                if find(row, col, 0):
                    return True

        return False