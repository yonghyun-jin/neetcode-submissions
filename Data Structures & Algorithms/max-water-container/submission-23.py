class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) -1
        area= 0
        max_area = 0
        while l < r:
            if heights[l] < heights[r]: 
                area = min(heights[r],heights[l])*(r-l)
                max_area = max(area,max_area)
                l = l+1
            else:
                area = min(heights[r],heights[l])*(r-l)
                max_area = max(area,max_area)
                r = r-1
        return max_area
            
