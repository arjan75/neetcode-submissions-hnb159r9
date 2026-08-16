class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        wordSet = set(wordDict)
        memo = {}

        def backtrack(i):
            if i == len(s):
                return [""]
            
            if i in memo:
                return memo[i]
            
            result = []
            for j in range(i, len(s)):
                word = s[i:j+1]
                if word not in wordSet:
                    continue
                
                restOfList = backtrack(j+1)

                if not restOfList:
                    continue
                
                for substr in restOfList:
                    sentence = word
                    if substr:
                        sentence += " " + substr
                    result.append(sentence)

            memo[i] = result
            return result

        return backtrack(0)
        