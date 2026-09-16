class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(idx, curr, target):
            if target == 0:
                result.append(curr.copy())
                return
            
            if idx >= len(nums) or target <= 0:
                return

            curr.append(nums[idx])
            dfs(idx, curr, target - nums[idx])
            curr.pop()
            dfs(idx + 1, curr, target)

        dfs(0, [], target)
        return result