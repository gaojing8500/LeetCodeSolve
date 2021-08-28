# class TrieNode(object):
#     def __init__(self, value=None):
#         self.trie = TrieNode()
#         self.value = value
import collections


class Trie(object):
    def __init__(self):
        self.child = collections.defaultdict(dict)
        self.return_result = []

    def insert(self, words):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        newnode = self.child
        for token in words:
            if token not in newnode.keys():
                newnode[token]= collections.defaultdict(dict)
            newnode = newnode[token]
        newnode["is_word"] = "is_word"

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        nownode = self.child
        for token in word:
            if token in nownode.keys():
                nownode = nownode[token]
            else:
                return False
        self.test_search(nownode)
        print(self.return_result)

    def test_search(self,nownode):
        for index in nownode.keys():
            if index != "is_word":
                self.return_result.append(index)
                self.test_search(nownode[index])
            else:
                self.return_result.append("###")
        # return "is_word" in nownode.keys()

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        nownode = self.child
        for token in prefix:
            if token in nownode.keys():
                newnode = newnode[token]
            else:
                return False
        return True
