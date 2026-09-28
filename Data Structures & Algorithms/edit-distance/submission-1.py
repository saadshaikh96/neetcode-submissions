class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        edits = [[0] * (len(word1) + 1) for i in range(len(word2) + 1)]
        edits[0][0] = 0

        for i in range(1, len(word1) + 1):
            edits[0][i] = edits[0][i - 1] + 1
        
        for i in range(1, len(word2) + 1):
            edits[i][0] = edits[i - 1][0] + 1

        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word1[j - 1] == word2[i - 1]:
                    edits[i][j] = edits[i - 1][j - 1]
                else:
                    edits[i][j] = 1 + min(edits[i - 1][j], edits[i][j - 1], edits[i - 1][j - 1])

        return edits[-1][-1]