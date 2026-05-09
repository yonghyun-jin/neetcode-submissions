class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # There could be multiple answers
        # So return smaller index
        # Are they sorted?, 
        # Duplicate number? 
        result = []

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                print("--")
                print("pair:",i,j)
                if nums[i] + nums[j] == target:
                    return [i,j]

        return[]

