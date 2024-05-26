class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def solve(n:int,arr:List[int],com:List[int],i:int,j:int,target:int,ans:List[List[int]]):
            #print(com,target)
            if target==0 :
                newlist = [word for word in com if word != 0]
                ans.append(newlist)
                com[j-1]=0
                j=j-2
                return
            if i==n or target<0:
                com[j-1]=0
                j=j-2
                return
            else:
                com[j]=arr[i]
                #print(com)
                solve(n,arr,com,i,j+1,target-arr[i],ans)
                solve(n,arr,com,i+1,j,target,ans)
        ans=[]
        com=[0]*100
        solve(len(candidates),candidates,com,0,0,target,ans)
        return ans

        