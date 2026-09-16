class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(idx, combination):
            if len(combination) == len(digits):
                result.append("".join(combination))
                return

            for letter in digitMap[digits[idx]]:
                combination.append(letter)
                dfs(idx + 1, combination)
                combination.pop()

        dfs(0, [])
        return result