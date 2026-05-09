class Solution:
    def trap(self, height: List[int]) -> int:
        #  we need left and min height of (right, left) - current position block
        left_max =[0]*len(height)    # 0, 2, 2, 3, 3, 3, 3, 3, 3, 3
        right_max =[0]*len(height)     # 3, 3, 3, 3, 3, 3, 3, 2, 1, 0

        

        left_value =0
        right_value = 0

        for index, item in enumerate(height):
            left_value = max(left_value, item)
            left_max[index] = left_value
        print(left_max)
        
        
        for index, value in enumerate(reversed(height)):
            right_value = max(right_value, value)
            print(index)
            right_max[len(height) - index -1] = right_value       
        print(right_max)

        res = 0
        water= 0

        for index, item in enumerate(height):
            water = min(left_max[index], right_max[index]) - item

            if water > 0 :
                res = res+water
            else:
                continue
        return res
        


            
        
        
        



         


                    
