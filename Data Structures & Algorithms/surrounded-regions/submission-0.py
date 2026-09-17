class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or i == ROWS - 1 or j == 0 or j == COLS - 1 and board[i][j] == 'O':
                    self.dfs(i, j, board)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
        

    def dfs(self, r, c, board):
        ROWS, COLS = len(board), len(board[0])
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != 'O':
            return
        board[r][c] = 'Y'
        self.dfs(r + 1, c, board)
        self.dfs(r - 1, c, board)
        self.dfs(r, c + 1, board)
        self.dfs(r, c - 1, board)

