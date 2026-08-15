class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        leftMax = height[left]
        rightMax = height[right]

        water = 0
        while left < right:
            if height[left] < height[right]:
                leftMax = max(height[left], leftMax)
                water += leftMax-height[left]
                left += 1
            else:
                rightMax = max(height[right], rightMax)
                water += rightMax-height[right]
                right -= 1
        return water
                

        