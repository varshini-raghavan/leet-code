class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        def check(grid):
            for row in grid:
                for i in row:
                    if i==0:
                        return False
            return True
        def solve(grid,n,m,r,c,v:int):
            if r==-1 or c==-1 or r==n or c==m or grid[r][c]==-1:
                return
            elif grid[r][c]==2 and check(grid):
                v.append(1)
            else:
                temp=grid[r][c]
                grid[r][c]=-1
                solve(grid,n,m,r+1,c,v)
                solve(grid,n,m,r-1,c,v)
                solve(grid,n,m,r,c+1,v)
                solve(grid,n,m,r,c-1,v)
                grid[r][c]=temp    
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    i1=i
                    j1=j
        v=[]
        solve(grid,n,m,i1,j1,v)
        return len(v)
        