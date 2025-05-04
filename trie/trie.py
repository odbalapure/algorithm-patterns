class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word
        Time: O(w)
        Space: O(1)
        NOTE: `TrieNode` is not counted as part of the auxiliary space
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word):
        """
        Search a complete word
        Time: O(w)
        Space: O(1)
        NOTE: `TrieNode` is not counted as part of the auxiliary space
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def starts_with(self, prefix):
        """
        Search for a prefix
        Time: O(w)
        Space: O(1)
        NOTE: `TrieNode` is not counted as part of the auxiliary space
        """
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
