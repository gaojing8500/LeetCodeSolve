class NumbersSum(object):
    def twoSum_base(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ##暴力遍历
        result_add = []
        for index,value in enumerate(nums):
            label = index + 1
            while(label < len(nums)):
                tmpadd = value + nums[label]
                if tmpadd == target:
                    result_add.append(index)
                    result_add.append(label)
                label+=1
        return result_add

    def twoSum_map(self,nums,target):
        '''
        Args:
            nums:
            target:

        Returns:
        '''
        ##其实并不需要双循环,采用dict来做
        num_map = {}
        for index, num in enumerate(nums):
            anth_num = target - num
            if anth_num in num_map:
                return [num_map[anth_num], index]
            num_map[num] = index



