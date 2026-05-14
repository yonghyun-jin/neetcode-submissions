class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = set()

        for item in nums:
            if item in d:
                return True
            else:
                d.add(item)
        return False