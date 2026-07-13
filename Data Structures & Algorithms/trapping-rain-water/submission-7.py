class Solution:
    def trap(self, height: List[int]) -> int:
        # water = min(tallest_right,tallest_left) - height[i]
        n = len(height)
        left = 0 
        right = n - 1
        maxleft = height[left]
        maxright = height[right]
        result = 0
        while left < right:
            if maxleft < maxright:
                left += 1
                maxleft = max(maxleft, height[left] )
                result += maxleft - height[left]
            else: 
                right -= 1
                maxright = max(maxright, height[right])
                result += maxright - height[right]
        return result
