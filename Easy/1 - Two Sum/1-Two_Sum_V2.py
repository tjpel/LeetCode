class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        map = {}

        for i, n in enumerate(nums):
            difference = target - n

            if difference in map:
                return[map[difference], i]
            
            map[n] = i

