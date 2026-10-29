class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]
        current.is_end = True


 
    def search(self, word: str) -> bool:
        def dfs(current:TrieNode,index):

            if index == len(word):
                return current.is_end

            char = word[index]

            if char == '.':
                for child in current.children.values():
                    if dfs(child,index+1):
                        return True

                return False

            if char not in current.children:
                return False

            return dfs(current.children[char],index +1)
        
        return dfs(self.root,0)
