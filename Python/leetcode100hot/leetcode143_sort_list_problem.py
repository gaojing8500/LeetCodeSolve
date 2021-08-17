
from ..base import LeetCodeBase

from typing import List

class ListNode(object):
    def __init__(self,val,next = None):
        self.node = val
        self.next = next

class SortList(LeetCodeBase):
    """[summary] 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

    输入：head = [4,2,1,3]
    输出：[1,2,3,4]

    Args:
        LeetCodeBase ([type]): [description]
    """    
    def __init__(self):
        self.name = "leetcode 143 排序链表"
    def __str__(self) -> str:
        return self.name
    def __call__(self, *args, **kwds):
        return "排序链表"

    def sort_list(self,list_node:List[int]):
        return "实现排序链表"
