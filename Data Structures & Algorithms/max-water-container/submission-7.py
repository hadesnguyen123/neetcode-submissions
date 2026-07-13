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
        l = 0 
        r = len(heights) - 1
        res = 0
        while r > l:
            area = min(heights[r],heights[l])*(r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l +=1
            else :
                r -=1
        return res
        
        
        