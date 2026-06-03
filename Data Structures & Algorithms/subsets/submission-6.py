class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        
        def dfs(i): # index of the value we make decision on
            if i >= len(nums): # I will tell us which element we are visiting
                # if i bigger or equal to the nums length , is out of bounce
                # When we reach to this point we know we got to the point where we have to append the result
                res.append(subset.copy())
                return
            # This is decision to include nums[i]
            # It is left decision
            subset.append(nums[i])
            dfs(i+1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res
            


        

# [
#  [],
#  [1],
#  [2],
#  [3],
#  [1,2],
#  [1,3],
#  [2,3],
#  [1,2,3]
# ]