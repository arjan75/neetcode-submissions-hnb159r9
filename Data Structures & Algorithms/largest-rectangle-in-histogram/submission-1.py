class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        length = len(heights)

        for i in range(len(heights)):
            currentHeight = heights[i]
            startIndex = i
            while stack and stack[-1][0] > currentHeight:
                item = stack.pop()
                itemHeight = item[0]
                itemIndex = item[1]

                maxArea = max(maxArea, itemHeight*(i-itemIndex))
                startIndex = itemIndex

            stack.append([currentHeight, startIndex])
        
        for item in stack:
            itemIndex = item[1]
            itemHeight = item[0]

            maxArea = max(maxArea, itemHeight*(length-itemIndex))
        return maxArea



        