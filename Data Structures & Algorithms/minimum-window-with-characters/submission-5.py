class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        for char in t:
            if char in tMap:
                tMap[char] += 1
            else:
                tMap[char] = 1
        
        formed = 0
        numberOfDistinct = len(tMap)
        currentWindow = {}

        left = 0
        right = 0
        minimumString = ""
        minimumLength = float('inf')

        while right < len(s):
            if s[right] in currentWindow:
                currentWindow[s[right]] += 1
            else:
                currentWindow[s[right]] = 1
            
            if s[right] in tMap and currentWindow[s[right]] == tMap[s[right]]:
                formed += 1
            
            while formed == numberOfDistinct:
                if s[left] in tMap and currentWindow[s[left]] == tMap[s[left]]:
                    formed -= 1

                currentWindow[s[left]] -= 1
                if minimumLength > right-left+1:
                    minimumLength = right - left + 1
                    minimumString = s[left:right+1]
                left += 1
            
            right += 1
        return minimumString
                

        
        