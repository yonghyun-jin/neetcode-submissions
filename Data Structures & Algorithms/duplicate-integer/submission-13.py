class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}

        for num in nums:
            my_dict[num] = "exist"
        
        if len(my_dict) != len(nums):
            return True
        return False