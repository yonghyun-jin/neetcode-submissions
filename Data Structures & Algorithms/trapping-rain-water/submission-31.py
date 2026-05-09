class Solution:
    def trap(self, height: List[int]) -> int:
        # 12:55
        # Finding the area
        # width of the container x min height of (left,right) - block

        # You cannot trab water if min(left, right) = 0
        
        # left  0  0  2  2  3  3  3  3  3
        # right 3  3  3  3  3  3  2  1  0
        # min   0  0  2  0  3  3. 2. 1. 0
        # block 0  2  0  3  2  0. 3. 2. 1
        # water 0 -2  2 -3  2  3 -1 -1 -1

        # psudo code
        max_left = []
        max_right = [0]* len(height)

        left = 0
        right = 0

        # Right Max Array
        for index,item in enumerate(height):
            if index==0:
                max_left.append(left)
            else:
                left = max(left, height[index-1])
                max_left.append(left)

        print(max_left) 
        # Left Max Array
        pointer = len(height)-1

        while 0 < pointer:
            if pointer==(len(height)-1):
                max_right[pointer] = right
                pointer = pointer -1
            else:
                right = max(right, height[pointer+1])
                max_right[pointer] = right
                pointer = pointer -1
        max_right[pointer] = right

        print(max_right)

        # Finding the sum of water

        water= 0

        for i in range(0,len(height)):
            # width of the container x min height of (left,right) - block

            area = 1*min(max_right[i], max_left[i]) - height[i]
            if area > 0:
                water = water+ area
            else:
                continue

        return water


            
        
        
        



         


                    
