class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
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
                
                remaining = backtrack(j+1)

                if not remaining:
                    continue
                
                for nextWord in remaining:
                    current = word
                    if nextWord:
                        current += (" " + nextWord)
                    result.append(current)
            memo[i] = result
            return result

        return backtrack(0)

        