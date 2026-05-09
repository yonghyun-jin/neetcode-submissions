class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_value = 0
        l=0
        while l < len(heights):
            r = l+1
            while r < len(heights):
                print("left:", l )
                print("right:",r)
                shorter = min(heights[l],heights[r])
                area = (r-l)*shorter
                print("area:", area)
                max_value = max(max_value, area)
                r=r+1
            l = l+1
        return max_value
