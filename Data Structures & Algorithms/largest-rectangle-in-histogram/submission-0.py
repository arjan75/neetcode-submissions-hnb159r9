class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        length = len(heights)
        for i in range(length):
            currentHeight = heights[i]
            currentIndex = i 
            start = i
            while stack and stack[-1][0] >= currentHeight:
                item = stack.pop()
                itemIndex = item[1]
                itemHeight = item[0]

                maxArea = max(maxArea, itemHeight*(currentIndex-itemIndex))
                start = itemIndex
            
            stack.append([currentHeight, start])
        
        for item in stack:
            maxArea = max(maxArea, item[0]*(length-item[1]))
        return maxArea
            

        