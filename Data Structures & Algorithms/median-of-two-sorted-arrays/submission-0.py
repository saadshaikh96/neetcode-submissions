class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        smallArray = nums1 if len(nums1) <= len(nums2) else nums2
        bigArray = nums1 if len(nums1) > len(nums2) else nums2

        middleIdx = (len(nums1) + len(nums2)) // 2

        left, right = 0, len(smallArray) - 1
        while True:
            smallMiddle = (left + right) // 2
            bigMiddle = middleIdx - smallMiddle - 2

            smallLeftMax = smallArray[smallMiddle] if smallMiddle >= 0 else float("-inf")
            smallRightMin = smallArray[smallMiddle + 1] if smallMiddle + 1 < len(smallArray) else float("inf")

            bigLeftMax = bigArray[bigMiddle] if bigMiddle >= 0 else float("-inf")
            bigRightMin = bigArray[bigMiddle + 1] if bigMiddle + 1 < len(bigArray) else float("inf")

            if smallLeftMax <= bigRightMin and bigLeftMax <= smallRightMin:
                if (len(nums1) + len(nums2)) % 2:
                    return min(smallRightMin, bigRightMin)
                return (max(smallLeftMax, bigLeftMax) + min(smallRightMin, bigRightMin)) / 2
            elif smallLeftMax > bigRightMin:
                right = smallMiddle - 1
            else:
                left = smallMiddle + 1