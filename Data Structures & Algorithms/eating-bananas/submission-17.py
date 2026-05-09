class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            # mid point
            m = (l + r)//2
            totalTime = 0
            for item in piles:
                totalTime += item // m
                if item % m != 0:  
                    totalTime += 1
            if totalTime > h:
                l = m +1
            else:
                
                r = m - 1
                res = m
        return res
            


        