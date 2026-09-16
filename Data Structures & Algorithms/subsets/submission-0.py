class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            subsetsWithNum = []
            for subset in result:
                subsetsWithNum.append(subset + [num])
            result.extend(subsetsWithNum)
        
        return result
