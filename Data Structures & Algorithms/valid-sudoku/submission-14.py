class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        s1 = set()
        s2 = set()
        s3 = set()

        x=0
        y=0

        while x < 9 and y < 9:
            for i in range(x, x + 3):  # Iterate through rows of the current 3x3 box
                for j in range(y, y + 3):  # Iterate through columns of the current 3x3 box
                    if board[i][j] in s1:  # Check for duplicates
                        return False
                    elif board[i][j] != ".":  # Add only non-empty values
                        s1.add(board[i][j])
                        print(i, j)  # Debugging: Print the current position

            # Move to the next 3x3 box
            x += 3
            if x >= 9:  # If x exceeds the grid, reset x and move to the next row of boxes
                x = 0
                y += 3
            s1.clear()  # Reset the set for the next 3x3 box
                
        # Check Logitude

        for line in board : 
            for item in line : 
                if item in s2:
                    return False
                else :
                    if item != ".":  
                        s2.add(item)
            s2.clear()

        # Check Latitude

        for index in range(0,len(board)-1): 
            for line in board:
                if line[index] in s3:
                    return False
                else :
                    if line[index] !=".":  
                        s3.add(line[index])
            s3.clear()
        
        return True


        # Big O : speed : 3N^2 Memory is Log N since I am gona use map
