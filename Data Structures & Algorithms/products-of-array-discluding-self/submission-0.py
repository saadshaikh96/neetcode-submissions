class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        productSoFar = 1
        for i in range(len(nums)):
            products[i] = productSoFar
            productSoFar *= nums[i]
        
        productSoFar = 1
        for i in reversed(range(len(nums))):
            products[i] *= productSoFar
            productSoFar *= nums[i]
            
        return products