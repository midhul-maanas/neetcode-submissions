class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i,x,y):
            if i == len(word):
                return True
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                return False
            if word[i] != board[x][y]:
                return False
            temp = board[x][y]
            board[x][y] = "#"  #Mark visited: to avoid reusing same cell, ensures forward movement only
            found = (backtrack(i+1,x-1,y) or backtrack(i+1,x+1,y) or backtrack(i+1,x,y-1) or backtrack(i+1,x,y+1))
            board[x][y] = temp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(0,i,j):
                    return True
        return False