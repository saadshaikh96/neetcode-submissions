class Solution:
    def canJump(self, nums: List[int]) -> bool:
        targetIndex = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            if i + nums[i] >= targetIndex:
                targetIndex = i

        return targetIndex == 0