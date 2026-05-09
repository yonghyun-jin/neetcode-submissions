class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        # We want to access the item each time
        for item in nums:
            if item in seen:
                return True
            else:
                seen[item] = True
        
        return False
        # 