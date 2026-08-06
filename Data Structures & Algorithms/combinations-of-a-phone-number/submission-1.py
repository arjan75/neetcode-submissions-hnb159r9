class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        if not digits:
            return []
        def traverseTree(index, curPath):
            if index == len(digits):
                result.append("".join(curPath))
                return
            
            char = digits[index]
            options = digitMap[char]
            for char in options:
                curPath.append(char)
                traverseTree(index+1, curPath)
                curPath.pop()
        
        traverseTree(0, [])
        return result
        