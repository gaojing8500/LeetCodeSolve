from Python.DataStructureAlgorithom.base_node_type_data_structure import ListNode
from Python.leetcode100hot.leetcode3_length_longest_substring import LengthLongestSubstring


def test_list_node():
    list_nodel = ListNode()
    list_nodel.add(2)
    list_nodel.add(3)
    print(len(list_nodel))




def test_leetcode3_length_long_substr(s):
    model = LengthLongestSubstring()
    print(model.solution_sliding_window_method("abcabcbb"))



if __name__ == '__main__':
    test_leetcode3_length_long_substr("pwwkew")

