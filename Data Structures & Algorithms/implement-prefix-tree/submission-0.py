class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        root = self.root
        for letter in word:
            if letter not in root:
                root[letter] = {}
            root = root[letter]
        root["*"] = word


    def search(self, word: str) -> bool:
        root = self.root
        for letter in word:
            if letter not in root:
                return False
            root = root[letter]  
        return "*" in root
        

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for letter in prefix:
            if letter not in root:
                return False
            root = root[letter]  
        return True

        