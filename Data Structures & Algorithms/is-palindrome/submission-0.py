class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not self.isAlphaNumeric(s[i]):
                i += 1
            while i < j and not self.isAlphaNumeric(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True

    def isAlphaNumeric(self, char):
        return (ord('a') <= ord(char.lower()) <= ord('z')) or \
        ord('0') <= ord(char) <= ord('9')