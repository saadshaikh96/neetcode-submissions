class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def dfs(nums, idx):
            if idx == len(nums):
                permutations.append(nums[:])
                return
            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                dfs(nums, idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]

        dfs(nums, 0)
        return permutations