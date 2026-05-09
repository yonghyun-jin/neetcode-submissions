from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []  # ✅ define result list
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # ✅ skip duplicate 'i' values
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum_num = nums[i] + nums[j] + nums[k]
                if sum_num == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # ✅ skip duplicate j and k
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif sum_num > 0:
                    k -= 1
                else:
                    j += 1
        
        return result
