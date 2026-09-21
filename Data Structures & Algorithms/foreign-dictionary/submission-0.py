class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        connections = {}

        for word in words:
            for char in word:
                if char not in connections:
                    connections[char] = set()

        for i in range(1, len(words)):
            word1, word2 = words[i - 1], words[i]
            minLength = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLength] == word2[:minLength]:
                return ""
            for j in range(minLength):
                if word1[j] != word2[j]:
                    connections[word1[j]].add(word2[j])
                    break
        
        visited = {}
        ordering = []

        for char in connections.keys():
            hasCycle = self.dfs(char, connections, visited, ordering)
            if hasCycle:
                return ""
        
        ordering.reverse()
        return "".join(ordering)

    def dfs(self, char, connections, visited, ordering):
        if char in visited:
            return visited[char]
        visited[char] = True

        for neighbor in connections[char]:
            hasCycle = self.dfs(neighbor, connections, visited, ordering)
            if hasCycle:
                return True

        visited[char] = False
        ordering.append(char)