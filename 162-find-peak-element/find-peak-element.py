class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak=0
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                peak=i
            else:
                return peak
        return peak

            