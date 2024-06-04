class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=[]
        l=0
        for i in nums:
            if i==1:
                l+=1
            else:
                res.append(l)
                l=0
        res.append(l)
        return max(res)