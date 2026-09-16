class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, currPattern = [], []

        def dfs(open, close):
            if open == 0 and close == 0:
                result.append("".join(currPattern))
                return

            if open > 0:
                currPattern.append('(')
                dfs(open - 1, close)
                currPattern.pop()
            
            if close > open:
                currPattern.append(')')
                dfs(open, close - 1)
                currPattern.pop()

        dfs(n, n)
        return result
        