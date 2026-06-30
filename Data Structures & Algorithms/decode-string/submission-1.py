class Solution:
    def decodeString(self, s: str) -> str:
        openBrackets = set()
        stack = []
        for i in range(len(s)):
            if s[i] == "]":
                value = ""
                while stack[-1] != "[":
                    item = stack.pop()
                    value = item + value
                stack.pop()


                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier
            
                stack.append(int(multiplier)*value)
            else:
                stack.append(s[i])
        
        concat = ""
        for i in range(len(stack)):
            concat += stack[i]
        return concat
        

            
        
                


        