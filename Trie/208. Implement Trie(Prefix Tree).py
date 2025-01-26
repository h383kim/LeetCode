################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/implement-trie-prefix-tree/
################################################################



class Trie:

    def __init__(self):
        # Initially Start with empty root node
        self.root = Node()

    def insert(self, word: str) -> None:
        # Start at the root
        cur = self.root
        for c in word:
            # If the path exists, char exists
            if c in cur.children:
                cur = cur.children[c] # Follow the path
            # If not,
            else:
                cur.children[c] = Node() # Create the new path
                cur = cur.children[c]    # Follow the path
        # Flag so that word is not in the trie
        cur.flag = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        
        # The word is found only if 
        # the end of the word we are searching is flagged
        return cur.flag

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        
        return True

class Node:
    def __init__(self):
        self.flag = False
        self.children = {}

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)