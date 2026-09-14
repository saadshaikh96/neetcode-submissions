class Solution:
    def findMin(self, nums: List[int]) -> int:
        minElement = float("inf")
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] <= nums[right]:
                minElement = min(minElement, nums[left])
                break
            
            mid = (left + right) // 2
            minElement = min(minElement, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return minElement