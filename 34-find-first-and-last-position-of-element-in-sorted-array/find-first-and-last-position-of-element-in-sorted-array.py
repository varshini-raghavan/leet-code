class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        c=nums.count(target)
        for i in nums:
            if i==target:
                s=nums.index(i)
        return [s,s+c-1]
            