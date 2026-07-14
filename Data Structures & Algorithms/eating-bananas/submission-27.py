class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r  # worst-case speed (always works)

        while l <= r:          # changed < to <=
            m = (l + r) // 2
            totalTime = 0
            for p in piles:
                totalTime += (p + m - 1) // m

            if totalTime <= h:      # fixed: compare to h, not to m
                res = m             # this speed works, try a slower one
                r = m - 1           # reduce upper bound
            else:                   # too slow
                l = m + 1           # increase lower bound
        
        return res