class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        unique = len(set(nums))
        if(n==unique):
            return False
        else:
            return True
        