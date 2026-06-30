class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return s

        def getPalindromeLength(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1:right]

        maxPalindrome = ""
        for i in range(len(s)):
            oddPalindrome = getPalindromeLength(i, i)
            evenPalindrome = getPalindromeLength(i, i+1)
            if len(oddPalindrome) > len(maxPalindrome):
                maxPalindrome = oddPalindrome
            
            if len(evenPalindrome) > len(maxPalindrome):
                maxPalindrome = evenPalindrome
        return maxPalindrome

        