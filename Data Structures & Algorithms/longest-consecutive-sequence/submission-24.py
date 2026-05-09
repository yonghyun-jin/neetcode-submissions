class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1:59
        # Returning length of consecutive sequence
        # 2:23


        # Edge case:
        # element is exactly great than the previous element 1:
        # if there is only 1 len(nums) we return 1

        # arr = sorted(nums)

        [2,20,4,10,3,4,5]
        [2,3,4,4,5,10,20]

        # 1 2 3 4 5
        # l = 0
        # r = l+1
        # max_count = 0
        # count = 0
        # while r < len(nums):
        # logic for updating each pointer
            # if nums[r-1] == nums[r]:
            # repetitive
            #  r = r+1
            # elif nums[r-1] +1 == nums[r]:
            #   count = count+1
            #   it means consecutive
            #   max_count = max ( max_count, count)
            #   r = r+1
            # else:
            #     l = r
            #     r = l+1
            #     count = 0
            # 
            # return max_count +1 
        l = 0
        r = l+1
        max_count = 1
        count = 1
        # if empty
        if len(nums)==1:
            return 1
        if len(nums)==0:
            return 0

        arr = sorted(nums)
        print(arr)
        while r < len(arr):
            if arr[r-1]==arr[r]:
                # repetitive number
                r = r+1
            elif arr[r-1]+1 ==arr[r]:
                # consecutive number
                count = count+1
                max_count = max(max_count,count)
                r = r+1
            else:
                max_count = max(max_count,count)
                l = r
                r = r+1
                count = 1

        return max_count




