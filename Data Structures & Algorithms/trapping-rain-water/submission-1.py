class Solution:
    def trap(self, height: List[int]) -> int:
        #idea: calculate trapped water in ith: area = min(heights[l], heights[r]) - heights[i]
        # bruth force:
        # res = 0
        # for i in range(len(height)):
        #     maxLeft = maxRight = height[i]
        #     for j in range(i):
        #         maxLeft = max(maxLeft,height[j])
        #     for j in range(i+1, len(height)):
        #         maxRight = max(maxRight,height[j])
        #     area = min(maxLeft, maxRight) - height[i]
        #     res += area
        # return res

        # using 2 pointer
        l = 0
        r = len(height) - 1
        maxl = height[l]
        maxr = height[r]
        res = 0
        while l < r:
            if maxl < maxr :
                l += 1
                maxl = max(maxl, height[l])
                res += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                res += maxr - height[r]
        return res

