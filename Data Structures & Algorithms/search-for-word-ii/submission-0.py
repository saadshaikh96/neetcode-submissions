class Trie:
    def __init__(self):
        self.root = {}

    def add(self, word):
        root = self.root
        for letter in word:
            if letter not in root:
                root[letter] = {}
            root = root[letter]
        root["*"] = word
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)

        visited = set()
        foundWords = set()
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                self.explore(i, j, board, visited, foundWords, trie.root)

        return list(foundWords)

    def explore(self, r, c, board, visited, foundWords, trieNode):
        if (r,c) in visited:
            return
        if board[r][c] not in trieNode:
            return

        letter = board[r][c]
        trieNode = trieNode[letter]
        if "*" in trieNode:
            foundWords.add(trieNode["*"])
        visited.add((r,c))
        for neighbor in self.getNeighbors(r, c, board):
            self.explore(neighbor[0], neighbor[1], board, visited, foundWords,  trieNode)
        visited.remove((r, c))

    def getNeighbors(self, r, c,  board):
        neighbors = []
        if r > 0:
            neighbors.append([r - 1, c])
        if r < len(board) - 1:
            neighbors.append([r + 1, c])
        if c > 0:
            neighbors.append([r, c - 1])
        if c < len(board[0]) - 1:
            neighbors.append([r, c + 1])

        return neighbors
        


