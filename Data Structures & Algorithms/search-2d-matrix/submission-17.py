from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        l, r = 0, len(matrix) - 1

        # Binary search to find the correct row
        while l <= r:
            m = l + (r - l) // 2
            if target > matrix[m][-1]:  # Target is greater than max value in row
                l = m + 1
            elif target < matrix[m][0]:  # Target is smaller than min value in row
                r = m - 1
            else:
                break  # Target is within this row

        if not (l <= r):  # If no valid row found
            return False
        
        row = matrix[m]
        l, r = 0, len(row) - 1

        # Binary search within the row
        while l <= r:
            mid = l + (r - l) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
