class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        x,y=0,0
        set3 = set()
        while x < 9 and y < 9:
            for i in range(x, x + 3):  # Iterate through rows of the current 3x3 box
                for j in range(y, y + 3):  # Iterate through columns of the current 3x3 box
                    if board[i][j] in set3:  # Check for duplicates
                        return False
                    elif board[i][j] != ".":  # Add only non-empty values
                        set3.add(board[i][j])
                        print(i, j)  # Debugging: Print the current position

            # Move to the next 3x3 box
            x += 3
            if x >= 9:  # If x exceeds the grid, reset x and move to the next row of boxes
                x = 0
                y += 3
            set3.clear()  # Reset the set for the next 3x3 box

            
                
        # x y
        # [0][0]
        # [1][0]
        # [2][0]
        # [0][1]
        # [1][1]
        # [2][1]
        set1 = set()
        set2 = set()
        

        # Validate Rows
        for y in range(0,9):
            for x in range(0,9):
                item = board[y][x]
                if item in set1 and item != ".":
                    return False
                else:
                    set1.add(item)
            set1.clear()

        # Validate Columns
        for x in range(0,9):
            for y in range(0,9):
                item = board[y][x]
                if item in set2 and item != ".":
                    return False
                else:
                    set2.add(item)
            set2.clear()

        return True
        
