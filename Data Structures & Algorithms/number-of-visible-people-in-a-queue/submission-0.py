class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        answer = [0] * len(heights)
        i = len(heights)-1
        stack = []

        while i >= 0:
            currentHeight = heights[i]
            visible = 0
            while stack and stack[-1] < currentHeight:
                stack.pop()
                visible += 1
            
            if stack:
                visible += 1
            
            stack.append(currentHeight)
            answer[i] = visible
            i -= 1
        return answer

        