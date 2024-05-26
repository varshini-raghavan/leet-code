class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 1
        prev = nums[0]
        if len(nums) == 1:
            return True
        if prev == 0:
            return False
        while i < len(nums)-1:
            prev = max(prev-1, nums[i])
            if not prev:
                return False
            i+=1        
        return True
            