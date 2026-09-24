class Solution:
    def countSubstrings(self, s: str) -> int:
        numPalindromes = 0

        for i in range(len(s)):
            numPalindromes += self.countPalindromes(s, i, i)
            numPalindromes += self.countPalindromes(s, i, i + 1)

        return numPalindromes

    def countPalindromes(self, s, left, right):
        numPalindromes = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            numPalindromes += 1
            left -= 1
            right += 1

        return numPalindromes