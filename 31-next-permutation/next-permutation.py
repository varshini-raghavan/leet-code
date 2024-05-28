class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        swap=-1
        ind=-1
        n=len(nums)-1
        for i in range(n,0,-1):
            if nums[i]>nums[i-1]:
                ind=i-1
                break
        for i in range(n,ind,-1):
            if nums[ind]<nums[i]:
                swap=i
                break
        if ind!=-1:
            nums[ind],nums[swap]=nums[swap],nums[ind]
            start=ind+1
            end=n 
            while(start<end):
                nums[start],nums[end]=nums[end],nums[start]
                start+=1 
                end-=1 
        else:
            nums.sort()



            
                

        