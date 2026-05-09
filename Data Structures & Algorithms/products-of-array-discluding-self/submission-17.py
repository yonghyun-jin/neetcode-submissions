class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            right = 1
            left = 1

            for j in range(0,i):
                right = right * nums[j]
            
            for k in range(i+1,len(nums)):
                left = left * nums[k]
            
            result.append(right * left)
        
        return result

            
