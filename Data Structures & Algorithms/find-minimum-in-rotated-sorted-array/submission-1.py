class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Iterate through the array
        # goal O(log n)
        # nums of array
        # return the min

        # [3,4,5,6,1,2]
        #    l      m      r
        #    7,0,1,2,3,4,5,6

        # first number at array.  len nums

        # 3 4 5 0 1 2
        # [3,4,5,6,1,2]

        # 

        # 4 5 6 7
        
        sort = sorted(nums)
        return sort[0]

