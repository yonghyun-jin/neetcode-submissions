class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_value = 0
        l=0
        r = len(heights)-1

        while l < r:
            lh = heights[l]
            rh = heights[r]
            min_value= min(lh,rh)
            area = (r-l)*min_value
            max_value = max(area, max_value)

            if rh > lh: 
                l+=1
            else:
                r-=1
            print("left: ", l)
            print("right: ", r)
            
        return max_value
