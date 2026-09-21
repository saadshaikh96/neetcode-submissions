class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n not in seen:
            seen.add(n)
            n = self.getSumOfSquares(n)
            if n == 1:
                return True

        return False

    def getSumOfSquares(self, num):
        sum = 0
        while num:
            digit = num % 10
            sum += digit ** 2
            num //= 10

        return sum