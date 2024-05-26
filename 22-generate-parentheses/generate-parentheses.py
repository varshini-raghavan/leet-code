class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(n: int, ans: List[str],x: List,op:int,cl:int,i:int):
            if cl==n:
                a=""
                for i in x:
                    a+=i
                ans.append(a)
            else:
                if op<n:
                    x[i]="("
                    solve(n,ans,x,op+1,cl,i+1)
                if op>cl:
                    x[i]=")"
                    solve(n,ans,x,op,cl+1,i+1)
        op=0
        cl=0
        ans=[]
        x=[None]*2*n
        solve(n,ans,x,op,cl,0)
        return ans

        