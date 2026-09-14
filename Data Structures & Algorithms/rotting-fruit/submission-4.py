from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        t = 0
        q = deque()
        fresh = 0
        ROWS,COLS = len(grid),len(grid[0])
        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))

                if grid[i][j] == 1:
                    fresh += 1
        
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
      
        while q and fresh > 0:
            for i in range(len(q)): # for time
                i,j = q.popleft()
                for dr,dc in directions:
                    r,c = dr + i, dc + j
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1 and (r,c) not in visited:
                        grid[r][c] = 2
                        q.append((r,c))
                        fresh -= 1
                        visited.add((r,c))
                        print(f"Visited: {visited}")
            t += 1
                    
        
        print(f"Fresh: {fresh} T:{t}")
        return t if fresh == 0 else -1
        

