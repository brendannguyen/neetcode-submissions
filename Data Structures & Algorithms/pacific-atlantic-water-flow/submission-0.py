class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic  = set()

        def dfs(r, c, ocean, prevHeight):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or prevHeight > heights[r][c] or (r, c) in ocean:
                return
            
            ocean.add((r,c))

            dfs(r+1, c, ocean, heights[r][c])
            dfs(r-1, c, ocean, heights[r][c])
            dfs(r, c+1, ocean, heights[r][c])
            dfs(r, c-1, ocean, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])
        
        result = []
        for c in range(COLS):
            for r in range(ROWS):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        
        return result

            

             
