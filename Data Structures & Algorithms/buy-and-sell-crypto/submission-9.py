class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        right_arr = []
        left_arr = []
        max_left = 0
        min_right = float('inf')
        res= 0

        for p in prices:
            min_right = min(min_right,p)
            right_arr.append(min_right)
        
        for p in reversed(prices):
            max_left = max(max_left,p)
            left_arr.append(max_left)

        print(left_arr)
        print(right_arr)
        

        for i in range(0, len(prices)):
            sum_val = left_arr[i] - right_arr[len(prices)-i-1]
            res = max(sum_val,res)
        return res




           
