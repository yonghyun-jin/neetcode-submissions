class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sort = sorted(set(nums))
        current = sort[0]
        max_value = 1
        count = 1

# 1 2 3 5 6 7 8
        for item in sort:
            print(item)
            if item != current+1:
                # if item not match
                max_value = max(max_value,count)
                count=1
            elif item == current+1:
                count = count+1
            current = item
        max_value = max(max_value,count)
        return max_value
