class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[(len(s))] = True

        j = len(s)
        while j >= 0:
            for word in wordDict:
                if j - len(word) >= 0:
                    if word == s[j-len(word):j]:
                        dp[j-len(word)] = dp[j-len(word)] or dp[j]
            j -= 1
        
        return dp[0] 


        
        