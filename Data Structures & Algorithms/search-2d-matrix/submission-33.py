class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first we need to find the what array to select

        # Next we run the binary search at arr

        for arr in matrix:
            r = arr[len(arr)-1]
            l = arr[0]

            if target >= l and target <= r:
                # Run binary search
                i = 0
                j = len(arr) -1 
                while i <= j: 
                    m = (i + j) //2
                    if arr[m] ==target:
                        return True
                    elif arr[m] < target:
                        i = m + 1
                    else:
                        j = m - 1
      
                return False
        return False