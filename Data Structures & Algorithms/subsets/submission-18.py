class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        save= []
        

        def dfs(i):
            if i == len(nums):
                res.append(save.copy())
                return

            save.append(nums[i])
            dfs(i+1)
            save.pop()
            dfs(i+1)

        dfs(0)
        return res
            
