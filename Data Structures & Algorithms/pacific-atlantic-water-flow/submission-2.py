class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS = len(heights),len(heights[0])
        pac,atl = set(),set()

        def dfs(r,c,visit,prevHeight):
            if (r,c) in visit or r not in range(ROWS) or c not in range(COLS) or heights[r][c] < prevHeight:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for c in range(COLS):
            dfs(0,c,pac,0)
            dfs(ROWS-1,c,atl,0)
        
        for r in range(ROWS):
            dfs(r,0,pac,0)
            dfs(r,COLS-1,atl,0)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res