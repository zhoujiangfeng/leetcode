'''
地址：https://leetcode-cn.com/problems/two-sum/
'''
# 暴力解法
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        for i in range(len(nums)):
            for j in range(1, len(nums[i:])):
                if nums[i] + nums[i + j] == target:
                    answer.append(i)
                    answer.append(i + j)
                    return answer
        return answer
