class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        while top <= bottom:
            targetRow = (top + bottom) // 2
            if target > matrix[targetRow][-1]:
                top = targetRow + 1
            elif target < matrix[targetRow][0]:
                bottom = targetRow - 1
            else:
                break

        if top > bottom:
            return False

        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[targetRow][mid]:
                left = mid + 1
            elif target < matrix[targetRow][mid]:
                right = mid - 1
            else:
                return True

        return False