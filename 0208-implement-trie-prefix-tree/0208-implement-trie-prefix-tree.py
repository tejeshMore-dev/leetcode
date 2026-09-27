class TrieNode:
    def __init__(self, val = None, isEnd = False):
        self.val = val
        self.childs = {}
        self.isEnd = isEnd
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char in node.childs:
                node = node.childs[char]
            else:
                new_node = TrieNode(char)
                node.childs[char] = new_node
                node = new_node
        
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char in node.childs:
                node = node.childs[char]
            else:
                return False
        
        return node.isEnd
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char in node.childs:
                node = node.childs[char]
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)