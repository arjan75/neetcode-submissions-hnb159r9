class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {"{": "}", "[": "]", "(": ")"}

        stack = []
        for char in s:
            if char in parenthesis:
                stack.append(char)
            else:
                if stack == []:
                    return False
                top = stack.pop()
                if parenthesis[top] != char:
                    return False
        return len(stack) == 0

        