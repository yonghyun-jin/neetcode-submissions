class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = {}
        for index, number in enumerate(numbers):
            if (target - number) in s:
                return [s[target - number]+1, index+1]
            else:
                s[number] = index
        
        return []

        