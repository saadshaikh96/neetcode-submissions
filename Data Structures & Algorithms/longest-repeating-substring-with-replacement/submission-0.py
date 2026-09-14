class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencyCount = {}
        result = 0
        left = 0
        maxFrequency = 0

        for right in range(len(s)):
            frequencyCount[s[right]] = frequencyCount.get(s[right], 0) + 1
            maxFrequency = max(maxFrequency, frequencyCount[s[right]])
            
            while (right - left + 1) - maxFrequency > k:
                frequencyCount[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)

        return result