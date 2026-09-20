class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxSum, maxEndingHere = nums[0], nums[0]
        for i in range(1, len(nums)):
            maxEndingHere = max(maxEndingHere + nums[i], nums[i])
            maxSum = max(maxSum, maxEndingHere)

        return maxSum