class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        left, right = 0, len(heights) - 1
        while left < right:
            top = min(heights[left], heights[right])
            width = right - left
            currentWater = top * width
            maxWater = max(maxWater, currentWater)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxWater