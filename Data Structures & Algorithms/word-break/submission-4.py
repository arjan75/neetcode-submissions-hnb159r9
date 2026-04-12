class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[-1] = True

        j = len(s)
        while j >= 0:
            for word in wordDict:
                if j - len(word) >= 0:
                    if s[j-len(word):j] == word:
                        dp[j-len(word)] = dp[j] or dp[j-len(word)]
            j -= 1
        return dp[0]
        