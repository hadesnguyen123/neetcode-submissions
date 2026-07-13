class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # calculate water: (right - left)
        # using bruth force : O(n^2) 
        # res = 0
        # for left in range(len(heights)):
        #     for right in range(len(heights)):
        #         area = min(heights[left],heights[right]) * (right - left)
        #         res = max(res, area)
        # return res
        # using 2 pointer
        left = 0
        right = len(heights) - 1
        res = 0
        while right > left:
            area = min(heights[right],heights[left]) * (right - left)
            res = max(res, area)
            if heights[left] <= heights[right] :
                left += 1
            else :
                right -=1
        return res
        
        
        