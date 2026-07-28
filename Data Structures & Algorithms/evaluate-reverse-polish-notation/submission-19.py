class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set()
        operators.add("+")
        operators.add("-")
        operators.add("/")
        operators.add("*")
        stack = []

        for token in tokens:
            if token in operators:
                first = stack.pop()
                second = stack.pop()
                if token == "+":
                    stack.append(str(int(first) + int(second)))
                
                elif token == "-":
                    stack.append(str(int(second) - int(first)))
                
                elif token == "*":
                    stack.append(str(int(second) * int(first)))
                
                elif token == "/":
                    if first == "0":
                        stack.append("0")
                    else:
                        stack.append(str(int(int(second) / int(first))))
            
            else:
                stack.append(token)
        
        return int(stack[0])



        