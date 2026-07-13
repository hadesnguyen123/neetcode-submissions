class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # calculate water: (right - left)
        # using bruth force : O(n^2) 
        res = 0
        for left in range(len(heights)):
            for right in range(len(heights)):
                area = min(heights[left],heights[right]) * (right - left)
                res = max(res, area)
        return res
        # using 2 pointer
        
        
        