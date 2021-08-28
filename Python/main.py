from Python.DataStructureAlgorithom.base_node_type_data_structure import ListNode
from Python.Trie.leetcode139_wordbreak import WordBreak, word_break_backtracking
from Python.Trie.trie import Trie
from Python.leetcode100hot.leetcode3_length_longest_substring import LengthLongestSubstring


def test_list_node():
    list_nodel = ListNode()
    list_nodel.add(2)
    list_nodel.add(3)
    print(len(list_nodel))




def test_leetcode3_length_long_substr(s):
    model = LengthLongestSubstring()
    print(model.solution_sliding_window_method("abcabcbb"))


def testRrie():
    trie = Trie()
    trie.insert("胶片打印")
    trie.insert("胶片")
    trie.insert("胶片打印常规流程")
    trie.insert("胶水")
    trie.search("胶")

def test_word_break():
    # s = "leetcode"
    # wordDict = ["leet", "code"]

    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]


    wordbreak = WordBreak(s,wordDict)
    # print(wordbreak.word_break())
    # print(word_break_backtracking(s))
    print(wordbreak.word_break_queue())
    print(wordbreak.word_break_dp())



if __name__ == '__main__':
    test_word_break()


