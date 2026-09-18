class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        connections = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                intermediate = word[:i]+ '*' + word[i+1:]
                connections[intermediate].add(word)

        queue = deque([[beginWord, 1]])
        visited = set()
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            if word in visited:
                continue
            visited.add(word)
            for i in range(len(word)):
                intermediate = word[:i]+ '*' + word[i+1:]
                for nextWord in connections[intermediate]:
                    queue.append([nextWord, steps + 1])
        
        return 0
        

        