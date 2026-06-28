class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and stack[-1][0] < temp:
                values = stack.pop()
                temperature = values[0]
                index = values[1]

                result[index] = i-index
            stack.append([temp, i])
        return result


        