class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def solve(n:int,arr:List[int],check:List[int],i:int,ans:List[List[int]]):
            if i==n:
                l=[]
                for j in range(n):
                    if check[j]!=-1:
                        l.append(arr[j])
                ans.append(l)
                return
            else:
                check[i]=1
                solve(n,arr,check,i+1,ans)
                check[i]=-1
                solve(n,arr,check,i+1,ans)
        ans=[]
        nums.sort()
        n=len(nums)
        check=[0]*n
        solve(n,nums,check,0,ans)
        return list(map(list, {tuple(i) for i in ans}))
