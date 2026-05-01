class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        for r in range(rows):
            for c in range (cols):
                if grid[r][c]==0:
                    q.append((r,c))
        def bfs(q):
            visited=[]
            while q:
                cur=q.popleft()
                visited.append(cur)
                print(q)
                r,c=cur[0],cur[1]
                if r+1<len(grid):
                    
                    if grid[r+1][c]==2147483647:
                        if (r+1,c) not in visited:
                            q.append((r+1,c))
                        grid[r+1][c]=grid[r][c]+1
                if c+1<len(grid[0]):
                    
                    if grid[r][c+1]==2147483647:
                        if (r,c+1) not in visited:
                            q.append((r,c+1))
                        grid[r][c+1]=grid[r][c]+1
                if c-1>=0:
                    
                    if grid[r][c-1]==2147483647:
                        if (r,c-1) not in visited:
                            q.append((r,c-1))
                        grid[r][c-1]=grid[r][c]+1
                if r-1>=0:
                    
                    if grid[r-1][c]==2147483647:
                        if (r-1,c) not in visited:
                            q.append((r-1,c))
                        grid[r-1][c]=grid[r][c]+1

        bfs(q)
        return
                    
        
        