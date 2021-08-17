class LengthLongestSubstring(object):
    def check_sub(self, sub_str):
        tmp_dict = {}
        for index, value in enumerate(sub_str):
            if value in tmp_dict:
                return 1
            tmp_dict[value] = index
        return 0

    def solution_brute_method(self, s):
        '''
        暴力法解决 复杂度较高 leetcode测试可能无法通过
        :param s: 输入list
        :return:
        '''
        str_list = list(s)
        tmp_len_sub = []
        if (len(str_list)) != 0:
            for j in range(len(str_list)):
                for i in range(len(str_list) - j):
                    count = i + j + 1
                    if count <= len(str_list):
                        tmp_sub_str = str_list[j:count]
                        if self.check_sub(tmp_sub_str):
                            continue
                        else:
                            tmp_len_sub.append(len(tmp_sub_str))
            tmp_len_sub.sort()
            return tmp_len_sub[len(tmp_len_sub) - 1]
        else:
            return 0

    def solution_map_method(self, s):
        pass

    def solution_sliding_window_method(self, s):
        if len(s) == 0:return 0
        lookup = set()
        left = 0
        max_len = 0
        curr_len = 0
        for index in range(len(s)):
            curr_len += 1
            while s[index] in lookup:
                lookup.remove(s[left])
                left +=1
                curr_len -= 1
            if curr_len > max_len:
                max_len = curr_len
            lookup.add(s[index])
        return max_len
