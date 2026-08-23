class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}

        def backtrack(i):
            if i == len(s):
                return [""]
            
            result = []
            if i in memo:
                return memo[i]

            for j in range(i, len(s)):
                word = s[i:j+1]
                if word not in wordSet:
                    continue

                remainingWords = backtrack(j+1)

                if not remainingWords:
                    continue
                
                for suffix in remainingWords:
                    sentence = word
                    if suffix:
                        sentence += " " + suffix
                    result.append(sentence)
            memo[i] = result
            return result

        return backtrack(0)

        