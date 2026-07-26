class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        output = ""
        for i in range(len(s)):
            if s[i] == "]":
                buildStr = ""
                while stack[-1] != "[":
                    item = stack.pop()
                    buildStr = item + buildStr 
                
                stack.pop()
                multiplier = ""
                while stack and stack[-1].isdigit():
                    item = stack.pop()
                    multiplier = item + multiplier
                
                stack.append(int(multiplier)*buildStr)
            
            else:
                stack.append(s[i])
        
        for i in range(len(stack)):
            output += stack[i]
        return output

                






        