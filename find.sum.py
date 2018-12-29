#!/usr/bin/env python
#coding=utf-8
'''
Created on  2018-12-29
@author: liubei
'''

import os
import sys
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range (len(nums)) :
            if ((target -nums[i] ) in nums):
                for j in range ((i+1),len(nums)):
                    if ( (nums[i] + nums[j]) == target):
                        result = [i,j]
                        return result

