class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area=0
        
        l=0
        r=len(heights) -1


        while l < r:
            width = r-l
            height = min(heights[l], heights[r])

            if heights[l] > heights[r]:
                r = r- 1
            else:
                l = l+ 1

            max_area = max( width*height, max_area)



        return max_area

