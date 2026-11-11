class Solution:
    def hammingWeight(self, n: int) -> int:
        numOneBits = 0
        while n:
            numOneBits += 1 if n & 1 else 0
            n >>= 1
        return numOneBits