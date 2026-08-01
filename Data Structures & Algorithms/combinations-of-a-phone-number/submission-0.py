class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsMap = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }

        result = []

        if digits == "":
            return []
        def dfs(index, curPath):
            if index == len(digits):
                result.append("".join(curPath))
                return

            recurseKey = digits[index]
            options = digitsMap[recurseKey]
            for i in range(len(options)):
                curPath.append(options[i])
                dfs(index+1, curPath)
                curPath.pop()
    
        dfs(0, [])
        return result
        