class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])

        def dfs(i, j, index):
            # Bound checking

            # when row is out of range(toward above)
            # when row is out of range(toward below)
            # when col is out of range(toward left)
            # when col is out of range(toward right)
            # when current index char is different from target char
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
                return False
            # index is last index
            if index == len(word) - 1:
                return True

            tmp = board[i][j]
            board[i][j] = '#'  # mark visited

            # 
            found = (dfs(i - 1, j, index + 1) or
                     dfs(i + 1, j, index + 1) or
                     dfs(i, j - 1, index + 1) or
                     dfs(i, j + 1, index + 1))

            board[i][j] = tmp  # unmark (backtrack)
            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False