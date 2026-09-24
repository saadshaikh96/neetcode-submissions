class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        start, end = 0, 0
        for i in range(len(s)):
            oddStart, oddLength = self.getLength(s, i, i)
            evenStart, evenLength = self.getLength(s, i, i + 1)

            if oddLength > maxLength:
                maxLength = oddLength
                start = oddStart
            if evenLength > maxLength:
                maxLength = evenLength
                start = evenStart

        return s[start : start + maxLength]

    def getLength(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return [left + 1, right - left - 1]