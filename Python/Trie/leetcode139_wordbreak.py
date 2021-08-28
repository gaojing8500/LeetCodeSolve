import queue
from queue import Queue


class WordBreak(object):
    def __init__(self, s, worddict):
        self.word_seq = s
        self.word_dict = worddict

    def word_break(self):
        '''
        https://leetcode-cn.com/problems/word-break/solution/shou-hui-tu-jie-san-chong-fang-fa-dfs-bfs-dong-tai/ 参考这个图解 DFS方式
        :return:
        '''
        if not self.word_seq:
            return True
        breap = [0]
        for i in range(len(self.word_seq) + 1):
            for j in breap:
                if self.word_seq[j:i] in self.word_dict:
                    breap.append(i)
                    break
        return breap[-1] == len(self.word_seq)

    def word_break_queue(self):
        '''
        采用队列的方式来做
        :return:
        '''
        ##采用一个先进先出的队列来做
        queue_ = Queue()
        queue_.put(0)
        tmp_list = [0]
        while queue_.qsize() != 0:
            start = queue_.get()
            if tmp_list[start]:
                continue
            tmp_list.insert(start, True)
            for i in range(len(self.word_seq) + 1):
                if self.word_seq[start:i] in self.word_dict:
                    if (i < len(self.word_seq)):
                        queue_.put(i)
                    else:
                        return True
        return False

    def word_break_dp(self):
        '''
        采用动态规划来做  动态规划思想是什么了 状态转移方程如何快速建立
        :return:
        '''
        length = len(self.word_seq)
        dp = [False] * (length+1)
        dp[0] = True
        for i in range(length):
            j = i - 1
            while j >= 0:
                if dp[i] == True:
                    break
                if dp[j] == False:
                    continue
                if self.word_seq[j:i] and dp[j] == True:
                    dp[i] = True
                    break
            j -= 1
        return dp[length]


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
model = WordBreak(s, wordDict)


def word_break_backtracking(word_seq):
    '''
        记忆回溯法 递归呀
        :return:
        '''
    if not word_seq:
        return True
    res = False
    for i in range(len(word_seq) + 1):
        if word_seq[:i] in model.word_dict:
            res = word_break_backtracking(word_seq[i:]) or res
    return res
