class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def solve(n:int,arr:List[int],check:List[int],i:int,ans:List[List[int]]):
            if i==n:
                l=[]
                for j in range(n):
                    if check[j]!=-1:
                        l.append(arr[j])
                ans.append(l)
            else:
                check[i]=1
                solve(n,arr,check,i+1,ans)
                check[i]=-1
                solve(n,arr,check,i+1,ans)
            
        check=[]
        ans=[]
        n=len(nums)
        check=[0]*n
        solve(n,nums,check,0,ans)
        return ans
