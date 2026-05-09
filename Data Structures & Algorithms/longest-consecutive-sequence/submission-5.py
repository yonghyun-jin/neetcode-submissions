class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # you can sort it first. and then calculate the longest consecutive
        max_value = 0
        arr = sorted(nums)
        print(arr)

        result = set()
        #  0 0 0 1 2 3 3 3 5 7 9 10 11 12 13 14  = 4 , 0123
        for item in arr :
            if len(result) == 0 or (item - 1) in result or item in result:
                result.add(item)
                max_value = max(max_value, len(result) )
            else:
                arr = result.clear()
                result.add(item)
        print(result)
        return max_value
            
