class Solution:
    def minWindow(self, s: str, t: str) -> str:
        currentWindow = {}
        requiredMap = {}
        for char in t:
            if char not in requiredMap:
                requiredMap[char] = 1
            else:
                requiredMap[char] += 1
        
        numberOfDistinctRequired = len(requiredMap)
        formed = 0
        
        right = 0
        left = 0

        minimumLength = float('inf')
        minString = ""
        while right < len(s):
            if s[right] in currentWindow:
                currentWindow[s[right]] += 1
            else:
                currentWindow[s[right]] = 1

            if s[right] in requiredMap and requiredMap[s[right]] == currentWindow[s[right]]:
                formed += 1

            
            while formed == numberOfDistinctRequired:
                currentWindow[s[left]] -= 1
                
                if s[left] in requiredMap and requiredMap[s[left]] > currentWindow[s[left]]:
                    formed -= 1
                    if currentWindow[s[left]] == 0:
                        del currentWindow[s[left]]

                
                if right-left+1 < minimumLength:
                     minimumLength = min(minimumLength, right-left+1)
                     minString = s[left:right+1]
                left += 1
            right += 1
            

        return minString



        


        