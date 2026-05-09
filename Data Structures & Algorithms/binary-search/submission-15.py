class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        
        while l <= r:
            m = l + (r - l) // 2
            # equal
            if nums[m] == target:
                return m

            elif nums[m] > target:
            # larger
                r = m -1
            # smaller
            else:
                l = m +1
        
        return -1
