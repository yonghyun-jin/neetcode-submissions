class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = sorted(nums)

        curr = 0
        count = 1
        result = 0

        for i,n in enumerate(arr):
            
            if i ==len(arr)-1:
                result = max(count, result)
                return result
            # [curr +1] = next value
            if n +1 == arr[i+1]:
                result = max(count, result)
                count = count +1
                continue
            # [curr +1 != next value] Not consecutive
            elif n == arr[i+1]:
                continue
            else:
                result = max(count, result)
                count = 1
                continue
        print(result)
        return result
            
