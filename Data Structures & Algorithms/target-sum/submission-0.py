class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        return self.dfs(0, 0, cache, nums, target)
        
    def dfs(self, idx, totalSoFar, cache, nums, target):
        if idx == len(nums):
            return 1 if totalSoFar == target else 0
        if (idx, totalSoFar) in cache:
            return cache[(idx, totalSoFar)]

        cache[(idx, totalSoFar)] = self.dfs(idx + 1, totalSoFar + nums[idx], cache, nums, target) + self.dfs(idx + 1, totalSoFar - nums[idx], cache, nums, target)

        return cache[(idx, totalSoFar)]