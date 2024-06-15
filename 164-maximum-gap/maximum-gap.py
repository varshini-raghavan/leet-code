class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        diff=0
        for i in range(1,len(nums)):
            temp=nums[i]-nums[i-1]
            diff=max(temp,diff)
        return diff