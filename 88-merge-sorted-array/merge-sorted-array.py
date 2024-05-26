class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = [i for i in nums1 if i != 0]
        for i in nums2:
            nums1.append(i)
        while(len(nums1)!=m+n):
            nums1.append(0)
        nums1.sort()
        return nums1

        