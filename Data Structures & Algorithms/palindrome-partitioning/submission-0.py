class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.dfs(0, s, result, [])
        return result

    def dfs(self, i, s, result, currentPath):
        if i >= len(s):
            result.append(currentPath.copy())
            return
        for j in range(i, len(s)):
            if self.isPalindrome(s, i, j):
                currentPath.append(s[i: j + 1])
                self.dfs(j + 1, s, result, currentPath)
                currentPath.pop()
    
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True