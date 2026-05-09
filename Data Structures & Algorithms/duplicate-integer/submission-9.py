class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for num in nums: 
            dictionary[num] = True  

        if len(dictionary) != len(nums):  
            return True  
        return False 