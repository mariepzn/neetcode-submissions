class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid :
            return 0 
        max_area=0
        def dfs(root):
            nonlocal max_area
            q=deque([root])
            area=0
            while q:
                cur = q.popleft()
                r,c=cur[0],cur[1]
                if grid[r][c]==1:
                    area+=1
                    grid[r][c]=0
                    if c+1<len(grid[0]):
                        q.append((r,c+1))
                    if r+1<len(grid):
                        q.append((r+1,c))
                    if r-1>0:
                        q.append((r-1,c))
                    if r-1>0:
                        q.append((r,c-1))
            max_area=max(max_area,area)
        rows=len(grid)
        cols=len(grid[0])
        for r in range (rows):
            for c in range (cols):
                if grid[r][c] ==1:
                    dfs((r,c))
        return max_area
                        



        
        
        