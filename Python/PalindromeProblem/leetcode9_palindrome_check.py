'''
Author: your name
Date: 2021-04-06 20:41:50
LastEditTime: 2021-04-19 21:01:48
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /LeetCodeSolve/Python/PalindromeProblem/palindrome_check.py
'''
from typing import Optional,Union
class ParlindromeCheck(object):
    """[summary] 回文数据检测，支持整型数据与字符串数据 主要核心思想 中心扩展思想 和暴力法

    Args:
        object ([type]): [description]
    """    
    def __init__(self):
        self.name = 'ParlindromeCheck support Int and String Input'
    
    def __str__(self):
        return self.name

    def __call__(self, input_data:Union[str,int]):
        print("调用check funtion")
    
    def palindrome_check(self,input_data:Union[str,int]):
        if isinstance(input_data,int):
            print("执行Int类型检查")
            return self.palindrome_check_int(input_data)
        if isinstance(input_data,str):
            print("执行string 类型检查")
            return self.palindrome_check_string(input_data)

    def palindrome_check_int(self,input_data:int):
        int_str = str(input_data)
        frist = 0
        end = len(int_str) - 1
        while(frist < end):
            if int_str[frist] != int_str[end]:
                return False
            frist = frist + 1
            end = end-1

        return True

    def palindrome_check_string(self,input_data:str):
        frist = 0
        end = len(input_data) - 1
        while(frist < end):
            if input_data[frist] != input_data[end]:
                return False
            frist = frist + 1
            end = end-1

        return True
            
        

if __name__ == '__main__':
    model = ParlindromeCheck()
    print(model)
    print(model.palindrome_check("121"))
    