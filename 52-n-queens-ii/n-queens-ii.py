class Solution:
    def totalNQueens(self, n: int) -> int:
        col=set()
        pd=set()#r+c
        nd=set()#r-c
        res=[]
        def backtrack(r):
            if r==n:
                res.append(1)
                return
            for c in range(n):
                if c in col or (r+c) in pd or (r-c) in nd:
                    continue
                col.add(c)
                pd.add(r+c)
                nd.add(r-c)
                backtrack(r+1)
                col.remove(c)
                pd.remove(r+c)
                nd.remove(r-c)
        backtrack(0)
        return len(res)