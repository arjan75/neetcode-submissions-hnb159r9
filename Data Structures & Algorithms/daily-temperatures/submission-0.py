class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        output = []
        for i in range(length):
            found = False
            for j in range(i+1, length):
                if temperatures[j] > temperatures[i]:
                    output.append(j-i)
                    found = True
                    break
            if not found:
                output.append(0)
        return output
            
                

        