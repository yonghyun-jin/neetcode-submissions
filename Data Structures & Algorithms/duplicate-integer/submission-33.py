class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #  Objective : find duplicate return false when nums
        
        d = {}

        for index, item in enumerate(nums):
            if item in d:
                return True
            else: 
                d[item] = index
        return False