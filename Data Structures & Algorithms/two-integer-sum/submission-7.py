class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # insert every number to the set
        # while inserting, find the other pair exist,
        # if exist return value of opposit pair and current pointer

        # let's use dict
        # my_dict = {} key = num value = index
        my_dict = {}

        for index, item in enumerate(nums):
            opp = target - item
            if opp in my_dict:
                return [my_dict[opp] ,index]
            my_dict[item] = index