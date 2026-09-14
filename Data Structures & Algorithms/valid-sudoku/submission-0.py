class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                currentValue = board[row][col]
                if currentValue == ".":
                    continue
                if currentValue in rows[row] or currentValue in cols[col] or currentValue in squares[(row//3, col//3)]:
                    return False

                rows[row].add(currentValue)
                cols[col].add(currentValue)
                squares[(row//3, col//3)].add(currentValue)

        return True

