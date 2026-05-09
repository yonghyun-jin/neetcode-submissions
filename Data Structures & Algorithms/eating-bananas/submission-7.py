class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r

        while l <= r:  # Fix condition to `<=`
            m = (l + r) // 2

            totalTime = 0
            for i in piles:
                totalTime += (i // m) + (1 if i % m else 0)  # Corrected calculation

            if totalTime > h:
                l = m + 1  # Increase `l` to search for a higher speed
            else:
                res = m  # Store the possible answer
                r = m - 1  # Search for a smaller speed
        return res



