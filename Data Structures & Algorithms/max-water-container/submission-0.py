class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # calculate water: (right - left)
        # using bruth force
        res = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                area = min(heights[j],heights[i]) * (j-i)
                res = max(res, area)
        return res    
        # using 2 pointer
        
        
        