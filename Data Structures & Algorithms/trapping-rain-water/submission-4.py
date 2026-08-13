class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        water = 0
        maxleft = height[left]
        maxRight = height[right]

        while left <= right:
            if height[left] < height[right]:
                maxleft = max(height[left], maxleft)
                water += maxleft-height[left]
                left += 1
            
            else:
                maxRight = max(height[right], maxRight)
                water += maxRight-height[right]
                right -= 1
        return water



        