class TrieNode(object):
    def __init__(self, value=None):
        self.__children = {}
        self.__value = value


class Trie(object):
    def __init__(self):
        self.node = TrieNode()

    def insert(self, words):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        for word in words:
            if self.node.__children is None:
                child = TrieNode(word)
                self.node.__children[word] = child
        return self.node

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
