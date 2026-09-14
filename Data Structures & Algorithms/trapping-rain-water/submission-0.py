class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        water = 0
        leftMax = [0] * len(height)
        leftMax[0] = height[0]
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * len(height)
        rightMax[-1] = height[-1]
        for i in reversed(range(len(height) - 1)):
            rightMax[i] = max(rightMax[i + 1], height[i])

        for i in range(len(height)):
            bound = min(leftMax[i], rightMax[i])
            water += bound - height[i]

        return water