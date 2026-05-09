class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = 0

        # expereiment -> Result Failed
        # if max_val samller move left, 
            # if left == right : move right
        # if max_val bigger, move right
        # if equal move right

        # max_val = 0

        # We have to know the min value from the right and max value from the left, 

        # right max - left min

        # right max
        # 10 7 7 7 7 1

        # Left min
        # 10 1 1 1 1 1

        # Expereiment
        # Get right max array
        # Get left max array

        # subtrct right max - left min

        # 2 5 7 8 10
        # 10 10 10 10 10

        arr1 = [0]*len(prices)     
        arr2 = [0]*len(prices)
        max_val = float('-inf')
        min_val = float('inf')

        res = 0

        # Find right max
        for i in range(len(prices)-1, -1, -1):
            max_val = max(max_val, prices[i])
            arr1[i] = max_val
        
        print(arr1)

        # Find left min
        for i in range(0,len(prices)):
            min_val = min(min_val,prices[i])
            arr2[i] = min_val
        
        print(arr2)

        for i in range(0,len(prices)):
            subtract = arr1[i] - arr2[i]
            res = max(res, subtract)

        return res
            




        


