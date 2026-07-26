class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestCommonPrefix = ""
        shortest = float('inf')
        for i in range(len(strs)):
            shortest = min(shortest, len(strs[i]))
        
        for i in range(shortest):
            current = strs[0][i]
            for word in strs:
                if word[i] != current:
                    return longestCommonPrefix
            
            longestCommonPrefix += current
        return longestCommonPrefix
                






        