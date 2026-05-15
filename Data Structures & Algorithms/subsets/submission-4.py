class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset =[]

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy()) #????
                return
            
            # Decision to add
            subset.append(nums[i])
            dfs(i+1) # ???
            # Decision to not add
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
