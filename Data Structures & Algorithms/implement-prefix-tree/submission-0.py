class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        startNode = self.root
        for char in word:
            if char not in startNode.children:
                startNode.children[char] = TrieNode()
            startNode = startNode.children[char]
        startNode.isWord = True

    def search(self, word: str) -> bool:
        startNode = self.root
        for char in word:
            if char not in startNode.children:
                return False
            startNode = startNode.children[char]
        return startNode.isWord == True

    def startsWith(self, prefix: str) -> bool:
        startNode = self.root
        for char in prefix:
            if char not in startNode.children:
                return False
            startNode = startNode.children[char]
        return True
        
        