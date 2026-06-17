class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False] * len(nums)

        def backtrack(perm):
            if len(perm) == len(nums):
                # When it reach to max length of array
                # Save to the result
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if not pick[i]: # if pick[i] is false we proceed
                    # what do we need to proceed?
                    # add to the permutation
                    perm.append(nums[i]) # 
                    pick[i] = True

                    # Move to next bc we have 
                    backtrack(perm)

                    # Restore
                    perm.pop()

                    pick[i] = False

        # initiate backtrack
        backtrack([])
        return res