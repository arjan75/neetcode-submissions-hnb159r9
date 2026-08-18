class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def backtrack(i):
            if i == len(s):
                return [""]

            result = []
            for j in range(i, len(s)):
                word = s[i:j+1]

                if word not in wordDict:
                    continue
                
                remaining = backtrack(j+1)
                if not remaining:
                    continue
                
                for suffix in remaining:
                    sentence = word
                    if suffix:
                        sentence += " " + suffix
                    result.append(sentence)
            return result
        
        return backtrack(0)

        