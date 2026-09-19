class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = self.getPower(x, abs(n))
        return result if n >= 0 else 1 / result
        

    def getPower(self, x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        result = self.getPower(x * x, n // 2)
        return result if n % 2 == 0 else result * x 