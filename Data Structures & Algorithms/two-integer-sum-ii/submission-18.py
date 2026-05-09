class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = {}
        for index, item in enumerate(numbers):
            value = target - item
            
            if value in s:
                return [s[value], index+1]
            else:
                s[item] = index+1
        
        


        