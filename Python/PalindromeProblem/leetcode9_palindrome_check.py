'''
Author: your name
Date: 2021-04-06 20:41:50
LastEditTime: 2021-05-10 20:21:23
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

    def palindrome_check_center_method(self,input_data:Union[str,int]):
        """[summary] 采用中心对称原理向两边扩散

        Args:
            input_data (Union[str,int]): [description]
        """ 
        if isinstance(input_data,str):
            self.check_center_method(input_data)
        else:
            transfor_str = str(input_data)
            self.check_center_method(transfor_str)

    def check_center_method(self,input_data:str):
        input_data_length = len(input_data)
        if input_data_length % 2 == 0:
            #判断长度是奇数还是偶数
            index_ptr = input_data_length / 2
        else: 
            center_ptr = int((input_data_length-1)/ 2)
            i = 1
            j = 1
            for index in range(input_data_length -(center_ptr+1)):
                center_ptr_after = center_ptr + i
                center_ptr_before = center_ptr - j
                i = i+1
                j = j+1
                if input_data[center_ptr_after] == input_data[center_ptr_before]:
                    return True
                else:
                    return False
                
    

if __name__ == '__main__':
    model = ParlindromeCheck()
    print(model)
    print(model.palindrome_check_center_method("121"))
    