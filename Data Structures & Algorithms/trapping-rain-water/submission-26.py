class Solution:
    def trap(self, height: List[int]) -> int:
        # min(block[left],block[right])
        left_list = [0]*len(height)
        right_list = [0]*len(height)
        max_left = 0
        max_right = 0
        res=0

        for l in range(len(height)):
            max_left = max(max_left, height[l])
            left_list[l] = max(max_left, height[l])
        
        for r in reversed(range(len(height))):
            max_right = max(max_right,height[r])
            right_list[r] = max(max_right,height[r])
        
        print(left_list)
        print(right_list)

        for z in range(len(height)):
            subtract = min(right_list[z], left_list[z]) - height[z]

            if subtract > 0 :
                res = res + subtract
        return res
        
        
        
        



         


                    
