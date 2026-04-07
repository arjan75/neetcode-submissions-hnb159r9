class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = set()
        operator.add("+")
        operator.add("-")
        operator.add("/")
        operator.add("*")

        stack = []
        for token in tokens:
            if token in operator:
                curResult = 0
                item1 = int(stack.pop())
                item2 = int(stack.pop())

                if token == "+":
                    curResult = item1 + item2
                
                elif token == "*":
                    curResult = item1 * item2
                
                elif token == "-":
                    curResult = item2 - item1
                
                else:
                    if item1 == 0:
                        curResult = 0
                    else:
                        curResult = int(item2 / item1)
                
                stack.append(curResult)
            else:
                stack.append(token)
            print (stack)
        return int(stack[0])





        