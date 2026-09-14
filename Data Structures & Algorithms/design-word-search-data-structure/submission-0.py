class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        root = self.root
        for letter in word:
            if letter not in root:
                root[letter] = {}
            root = root[letter]

        root["*"] = word
        
    def search(self, word: str) -> bool:
        return self.dfs(0, word, self.root)

    def dfs(self, idx, word, root):
        currentNode = root
        for i in range(idx, len(word)):
            char = word[i]
            if char == ".":
                for key, nextNode in currentNode.items():
                    if key != "*" and self.dfs(i + 1, word, nextNode):
                        return True
                return False
            else:
                if char not in currentNode:
                    return False
                currentNode = currentNode[char]
        return "*" in currentNode
