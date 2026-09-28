class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lcs = [[0] * (len(text1) + 1) for i in range(len(text2) + 1)]

        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text2[i - 1] == text1[j - 1]:
                    lcs[i][j] = lcs[i-1][j-1] + 1
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], lcs[i-1][j-1])

        return lcs[-1][-1]