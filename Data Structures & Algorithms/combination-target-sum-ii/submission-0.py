class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(idx, nums, currentTarget):
            if currentTarget == 0:
                result.append(nums.copy())
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if currentTarget - candidates[i] < 0:
                    break

                nums.append(candidates[i])
                dfs(i + 1, nums, currentTarget - candidates[i])
                nums.pop()

        dfs(0, [], target)
        return result