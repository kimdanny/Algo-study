# https://leetcode.com/problems/implement-trie-prefix-tree/

class Node:
    def __init__(self):
        self.children = dict()
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            # swim down
            curr = curr.children[c]
        
        # curr is now set to the last char of word node
        curr.is_word = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.is_word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True



trie =  Trie();
trie.insert("apple");
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app");
print(trie.search("app"))
