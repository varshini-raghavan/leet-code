class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solve(n:int,arr:List[int],start:int,end:int,ans:List[List[int]]):
            
            if start==end:
                ans.append(arr.copy())
                return
            else:
                for i in range(start,end):
                    arr[i],arr[start]=arr[start],arr[i]
                    solve(n,arr,start+1,end,ans)
                    arr[i],arr[start]=arr[start],arr[i]
        ans=[]
        solve(len(nums),nums,0,len(nums),ans)
        return ans
                    

                

        