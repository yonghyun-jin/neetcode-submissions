from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0  # handle empty input safely

        nums = sorted(set(nums))  # ✅ remove duplicates & sort
        print(nums)

        max_num = 1
        prev = 0
        init = 0

        for index, item in enumerate(nums):
            if index == 0:
                continue  # skip the first element, nothing to compare yet

            # ✅ consecutive
            if item == nums[prev] + 1:
                prev = index
                max_num = max(max_num, index - init + 1)

            # ❌ not consecutive
            else:
                init = index
                prev = index  # reset prev pointer too

        return max_num
