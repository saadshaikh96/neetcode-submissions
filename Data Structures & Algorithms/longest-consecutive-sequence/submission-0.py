class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {num: False for num in nums}
        longest = 0

        for num in nums:
            if seen[num]:
                continue
            range = self.getRange(num, seen)
            longest = max(longest, range)

        return longest

    def getRange(self, num, seen):
        left, right = num - 1, num + 1
        while left in seen and not seen[left]:
            seen[left] = True
            left -= 1

        while right in seen and not seen[right]:
            seen[right] = True
            right += 1

        return right - left - 1
