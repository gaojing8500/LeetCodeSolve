'''
线性数据结构比较简单，主要包含数组、链表、队列、栈、散列表和哈希表
'''
from Python.DataStructureAlgorithom.base_node_type_data_structure import ListNode


class SingleListNode(object):
    '''
    单链表结构 增删改查
    '''
    def __init__(self, node=None):
        self.head = node

    def __len__(self):
        length = 0
        cur_node = self.head
        while cur_node:
            length += 1
            cur_node = cur_node.next
        return length

    def add(self, value):
        ## head insert
        if value:
            node = ListNode(value)
            node.next = self.head
            self.head = node

    def append(self, value):
        ## tail insert
        if value:
            node = ListNode(value)
            curr = self.head
            if curr:
                while curr.next:
                    curr = curr.next
                curr.next = node
            else:
                self.head = node

    def insert(self,pos,value):
        ##具体位置上面插入一个数据元
        if pos <= 0:
            self.add(value)
        elif pos > self.__len__() - 1:
            self.append(value)
        else:
            node = ListNode(value)
            i = 0
            curr = self.head
            while curr:
                if i == pos - 1:
                    break
                curr = curr.next
                i += 1
            node.next = curr.next