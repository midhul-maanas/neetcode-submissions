from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
          return 0
        ROWS,COLS = len(grid),len(grid[0])
        visited = set()
        maxArea = 0

        def bfs(r,c):
            nonlocal maxArea
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            area = 1
            while q:
                row,col = q.popleft()
                directions = [(-1,0),(1,0),(0,-1),(0,1)]
                for dr,dc in directions:
                    r,c = row+dr,col+dc
                    if r in range(ROWS) and c in range(COLS) and (r,c) not in visited and grid[r][c] == 1:
                        q.append((r,c))
                        visited.add((r,c))
                        area += 1
            maxArea = max(maxArea,area)
                        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in visited:
                    bfs(i,j)
        return maxArea 