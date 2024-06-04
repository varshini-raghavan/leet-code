class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        ex=(n*(n+1))/2
        ac=0
        for i in nums:
            ac+=i
        return int(ex-ac)