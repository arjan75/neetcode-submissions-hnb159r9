class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindromesCentre(left, right):
            number = 0
            while left >= 0 and right < len(s) and s[right] == s[left]:
                left -= 1
                right += 1
                number += 1
            return number
        
        totalPalindromes = 0
        for i in range(len(s)):
            oddNumber = countPalindromesCentre(i, i)
            evenNumber = countPalindromesCentre(i, i+1)
            totalPalindromes += (oddNumber + evenNumber)
        return totalPalindromes


        