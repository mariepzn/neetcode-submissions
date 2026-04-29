class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited=set()
        rows,cols=len(grid),len(grid[0])
        islands=0
        def bfs(grid,root):
            queue = deque([root])
            while queue:
                cur=queue.pop()
                r,c=cur[0],cur[1]
                if grid[r][c]=='1':
                    if r+1<len(grid): 
                        if (r+1,c) not in visited:
                            queue.append((r+1,c))
                            visited.add((r+1,c))
                    if c+1<len(grid[0]):
                        if (r,c+1) not in visited:
                            queue.append((r,c+1))
                            visited.add((r,c+1))
                    if c-1>=0:
                        if (r,c-1) not in visited:
                            queue.append((r,c-1))
                            visited.add((r,c-1))
                    if r-1>=0:
                        if (r-1,c) not in visited:
                            queue.append((r-1,c))
                            visited.add((r-1,c))
                
                


        for r in range (rows):
            for c in range (cols):
                if grid[r][c]=='1' and (r,c) not in visited:
                    visited.add((r,c))
                    bfs(grid,(r,c))
                    islands+=1
        return islands