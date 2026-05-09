class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n^2) to access every element of array
        # and push the product result to the output array

        i = 0
        res = [0] * len(nums)
        
        while i < len(nums):
            product = 1
            l = 0
            while l < len(nums):
                if l == i:    
                    pass
                else:
                    product = product * nums[l]
                l+=1
            res[i] = product
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