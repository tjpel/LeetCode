"""
Author: Thomas Pelowitz
    Website: https://www.tpelowitz.com
    Github: https://www.github.com/tjpel
Date: 13NOV23

Problem link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""

class Solution:
    
    def removeDuplicates(self, nums: list[int]) -> int:
        lastNum = None
        k = 0
        
        for num in nums:
            if num != lastNum:
                nums[k] = num
                k += 1
            lastNum = num
                
        return k