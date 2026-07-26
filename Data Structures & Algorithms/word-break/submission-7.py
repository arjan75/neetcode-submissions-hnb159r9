class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]* (len(s)+1)
        dp[-1] = True

        i = len(dp)
        while i >= 0:
            for word in wordDict:
                if s[i-len(word):i] == word:
                    dp[i-len(word)] = dp[i] or dp[i-len(word)]
            i -= 1
        return dp[0] == True
        