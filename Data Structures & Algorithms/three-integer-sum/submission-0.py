class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum == 0:
                    triplets.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif currentSum < 0:
                    left += 1
                else:
                    right -= 1

        return [[i, j, k] for i,j,k in triplets]