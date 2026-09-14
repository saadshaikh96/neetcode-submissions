class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            possibleK = (left + right) // 2
            timeTaken = 0
            for pile in piles:
                timeTaken += math.ceil(pile / possibleK)
            
            if timeTaken <= h:
                result = possibleK
                right = possibleK - 1
            else:
                left = possibleK + 1

        return result