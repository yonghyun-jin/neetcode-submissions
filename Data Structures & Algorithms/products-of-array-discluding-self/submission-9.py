class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n^2) to access every element of array
        # and push the product result to the output array
        n = len(nums)
        res = [0] * n

        i = 0
        while i < n:
            prod = 1
            j = 0
            while j < n:
                if i != j:
                    prod *= nums[j]
                j += 1
            res[i] = prod
            i += 1

        return res
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         res = [0] * n

#         for i in range(n):
#             prod = 1
#             for j in range(n):
#                 if i == j:
#                     continue    
#                 prod *= nums[j]
            
#             res[i] = prod
#         return res