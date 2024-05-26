class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0 
        right = len(height) - 1
        while left < right:
            if height[left] > height[right]:
                area = height[right] * (right - left)
                right -= 1
            else:
                area = height[left] * (right - left)    
                left += 1 
            maxarea = max(maxarea, area)    
        return maxarea