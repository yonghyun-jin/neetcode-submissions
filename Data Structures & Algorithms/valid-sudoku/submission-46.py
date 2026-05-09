class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        arr1 = set()
        arr2 = set()
        arr3 = set()
        # Check longitude
        for i in range(0,9):
            arr1 = set()
            for item in board[i]:
                if item == ".":
                    continue
                if item in arr1:
                    return False
                else:
                    arr1.add(item)
            arr1.clear()
        
        # Check latitude
        for i in range(0,9):
            for j in range(0,9):
                item = board[j][i]
                if item == ".":
                    continue
                if item in arr2:
                    return False
                else:
                    arr2.add(item)
            arr2.clear()
    
        
        # Check 3x3 boxes
        for boxRow in range(0, 9, 3):      # 0,3,6
            for boxCol in range(0, 9, 3):  # 0,3,6
                arr3.clear()
                for x in range(boxRow, boxRow + 3):
                    for y in range(boxCol, boxCol + 3):
                        number = board[x][y]
                        if number == ".":
                            continue
                        if number in arr3:
                            return False
                        arr3.add(number)

        return True

            
            



            

        