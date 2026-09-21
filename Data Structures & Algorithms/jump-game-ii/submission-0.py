class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[0] = 0

        for currentPosition in range(1, len(nums)):
            for previousPosition in range(currentPosition):
                jumpFromPrevious = nums[previousPosition]
                if previousPosition + jumpFromPrevious >= currentPosition:
                    dp[currentPosition] = min(dp[currentPosition], 1 + dp[previousPosition])

        return dp[-1]
            