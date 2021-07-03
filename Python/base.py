'''
Author: your name
Date: 2021-07-03 15:36:48
LastEditTime: 2021-07-03 16:19:34
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /LeetCodeSolve/Python/base.py
'''
from abc import ABC, abstractmethod


class LeetCodeBase(ABC):
    @abstractmethod
    def __str__(self) -> str:
       pass
    @abstractmethod
    def __call__(self,*args,**kwds):
        pass