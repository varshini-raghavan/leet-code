class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=maxsum=nums[0]
        for i in range(1,len(nums)):
            if cur<0:
                cur=nums[i]
            else:
                cur=cur+nums[i]
            maxsum=max(maxsum,cur)
        return maxsum
