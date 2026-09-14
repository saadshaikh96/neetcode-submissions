class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagrams = defaultdict(list)

        for word in strs:
            counts = [0 for i in range(26)]
            for letter in word:
                counts[ord(letter) - ord('a')] += 1
            anagrams[tuple(counts)].append(word)

        return list(anagrams.values())
            
