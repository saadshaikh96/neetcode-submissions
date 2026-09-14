class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minWindow = [0, float("inf")]
        smallMap = {}
        for char in t:
            smallMap[char] = smallMap.get(char, 0) + 1

        uniqueFound, uniqueTarget = 0, len(smallMap)
        left, right = 0, 0
        bigMap = {}
        while right < len(s):
            currentChar = s[right]
            if currentChar not in smallMap:
                right += 1
                continue
            bigMap[currentChar] = bigMap.get(currentChar, 0) + 1
            if bigMap[currentChar] == smallMap[currentChar]:
                uniqueFound += 1

            while uniqueFound == uniqueTarget and left <= right:
                minWindow = min(minWindow, [left, right], key=lambda x: x[1]-x[0])
                leftChar = s[left]
                if leftChar not in smallMap:
                    left += 1
                    continue
                if bigMap[leftChar] == smallMap[leftChar]:
                    uniqueFound -= 1
                bigMap[leftChar] -= 1

                left += 1

            right += 1

        start, end = minWindow
        return "" if end == float("inf") else s[start:end + 1]
        