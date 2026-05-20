class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        length = len(heights)
        for i in range(length):
            currentHeight = heights[i]

            start = i
            while stack and stack[-1][0] > currentHeight:
                item = stack.pop()
                index = item[1]
                height = item[0]

                maxArea = max(maxArea, (i-index)*height)
                start = index
            stack.append([currentHeight, start])
        
        for item in stack:
            itemHeight = item[0]
            itemIndex = item[1]
            maxArea = max(maxArea, (length-itemIndex)*itemHeight)
        return maxArea


        