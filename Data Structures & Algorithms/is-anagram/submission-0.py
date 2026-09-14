class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}
        for char in s:
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
        
        for char in t:
            if char not in counts or counts[char] == 0:
                return False
            counts[char] -= 1
        
        for char in counts:
            if counts[char] != 0:
                return False
        
        return True