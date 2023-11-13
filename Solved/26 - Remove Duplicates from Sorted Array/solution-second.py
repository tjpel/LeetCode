"""
Author: Thomas Pelowitz
    Website: https://www.tpelowitz.com
    Github: https://www.github.com/tjpel
Date: 13NOV23

Problem link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""

class Solution:
    
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
                
        return k