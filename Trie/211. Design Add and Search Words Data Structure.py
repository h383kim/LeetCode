################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/design-add-and-search-words-data-structure
################################################################



class WordDictionary(object):

    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for i in word:
            if i in cur.children:
                cur = cur.children[i]
            else:
                cur.children[i] = Node()
                cur = cur.children[i]
        cur.flag = True

    def searchFrom(self, word, start):
        cur = start
        for idx, c in enumerate(word):
            if c == '.':
                for child in cur.children.values():
                    if self.searchFrom(word[idx + 1:], child):
                        return True
                return False
            else:
                if c in cur.children:
                    cur = cur.children[c]
                else:
                    return False
        
        return cur.flag

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.searchFrom(word, self.root)
    
        
class Node():
    def __init__(self):
        self.children = {}
        self.flag = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)