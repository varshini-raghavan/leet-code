class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        setlist=set(nums)
        m=1
        n=nums[0]
        for i in setlist:
            if m<nums.count(i):
                n=i
                m=nums.count(i)
        return n
            

        