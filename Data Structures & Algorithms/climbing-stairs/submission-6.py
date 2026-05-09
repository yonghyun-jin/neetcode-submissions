class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        
        dp = [0] * (n+1) #3
        # [0],[0],[0],[0]
        dp[1], dp[2] = 1, 2
        # [0],[1],[2],[0]

        # Bottom up approach
        for i in range(3,n+1):
            # we already filled out 0 1 2 
            # 3, 4, 5, ..., n
            # How we calculate from bottom up?
            # i = 3: dp[3] = dp[2] + dp[1] = 2 + 1 = 3 → dp = [0,1,2,3,0,0]
            # i = 4: dp[4] = dp[3] + dp[2] = 3 + 2 = 5 → dp = [0,1,2,3,5,0]
            # i = 5: dp[5] = dp[4] + dp[3] = 5 + 3 = 8 → dp = [0,1,2,3,5,8]
            dp[i] = dp[i-1] + dp[i-2] # we already have 01 2 
        return dp[n]