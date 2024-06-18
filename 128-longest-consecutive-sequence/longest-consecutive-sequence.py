class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        nums=list(set(nums))
        nums.sort()
        long=1
        mlong=1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                long+=1
            else:
                long=1
            mlong=max(mlong,long)
        return mlong
