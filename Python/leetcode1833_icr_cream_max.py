'''
Author: your name
Date: 2021-07-03 15:42:02
LastEditTime: 2021-07-03 17:02:04
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /LeetCodeSolve/Python/leetcode1833_icr_cream_max.py
'''
from typing import List
from base import LeetCodeBase
from typing import List
class IceCreamMaxNum(LeetCodeBase):
    def __init__(self):
        self.name = "leetcode 1833-ice cream max numbers"
    def __str__(self):
        return  self.name
    def __call__(self,*args,**kwds):
        return self.ice_cream_max_number(args[0],args[1])

    def ice_cream_max_number(self,coin:int,costs:List[int]):
        """[summary] 输入主要是两个 coin  cost
        输入：costs = [1,3,2,4,1], coins = 7
        输出：4
        解释：Tony 可以买下标为 0、1、2、4 的雪糕，总价为 1 + 3 + 2 + 1 = 7
        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/maximum-ice-cream-bars。

        一般的做法：
        1、排序+贪心法
        """
        sort_cost_list = self.sort_cost(costs)
        count = 0
        for cost in sort_cost_list:
            if(coin >= cost):
                coin -= cost
                count=count + 1
            else:
                break
        return count
    def sort_cost(self,costs:List[int]):
        costs.sort() 
        return costs

if __name__ == "__main__":
    ice_cream_model = IceCreamMaxNum()
    # costs = [1,3,2,4,1]
    # coins = 7
    # costs = [10,6,8,7,7,8]
    # coins = 5
    costs = [1,6,3,1,2,5]
    coins = 20
    print(ice_cream_model(coins,costs))


    