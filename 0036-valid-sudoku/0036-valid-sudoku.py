class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[i][j] not in visited or board[i][j] == ".":
                    visited.add(board[i][j])
                else:
                    return False

        for i in range(9):
            visited = set()
            for j in range(9):
                if board[j][i] not in visited or board[j][i] == ".":
                    visited.add(board[j][i])
                else:
                    return False
        
        for i in range(3):
            for j in range(3):
                visited = set()
                for k in range(i*3, i*3 + 3):
                    for l in range(j*3, j*3 + 3):
                        if board[k][l] not in visited or board[k][l] == ".":
                            visited.add(board[k][l])
                        else:
                            return False

        return True                        

        


