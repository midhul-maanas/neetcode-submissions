class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for r in range(n)] for c in range(n)]
        self.res =[]
        self.placeQueen(board,0,n)
        return self.res

    def placeQueen(self,board,col,n):
        if col == n:
            self.res.append(["".join(row) for row in board]) 
            return 
        for row in range(n):
            if self.isSafe(board,col,row,n):
                board[row][col] = 'Q'
                self.placeQueen(board,col+1,n)
                board[row][col] = '.'
    
    def isSafe(self,board,col,row,n): #check only the left side since filling is from left -> right and right is currently unfilled.
        for c in range(col):
            if board[row][c] == 'Q':
                return False
        for i,j in zip(range(row,-1,-1),range(col,-1,-1)): #upper left diagonal
            if board[i][j] == 'Q':
                return False
        for i,j in zip(range(row,n),range(col,-1,-1)): #lower left diagonal
            if board[i][j] == 'Q':
                return False
        return True

