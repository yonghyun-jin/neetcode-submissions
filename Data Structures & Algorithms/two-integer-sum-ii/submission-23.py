from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            sum_num = numbers[l] + numbers[r]

            # sum too big -> decrease by moving right pointer left
            if sum_num > target:
                r -= 1

            # sum too small -> increase by moving left pointer right
            elif sum_num < target:
                l += 1

            else:
                # Two Sum II expects 1-based indices
                return [l + 1, r + 1]

        return []
