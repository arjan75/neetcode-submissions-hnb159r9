class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            currentTemp = temperatures[i]

            while stack and stack[-1][0] < currentTemp:
                value = stack.pop()
                temp = value[0]
                index = value[1]

                result[index] = i-index
            stack.append([currentTemp, i])
        return result
        