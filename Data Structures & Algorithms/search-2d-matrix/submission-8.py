class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        res = -1
        Xlength = len(matrix)-1
        for Yindex, y in enumerate(matrix[::-1]):
            print("Y: ", y)
            if matrix[Yindex][0] <= target:
                for Xindex, x in enumerate(matrix[Yindex]):
                    print("X: ", x)
                    if x == target:
                        return True
        
        return False
            
            
