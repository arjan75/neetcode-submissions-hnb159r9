class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        for char in t:
            if char in tMap:
                tMap[char] += 1
            else:
                tMap[char] = 1
        
        numberOfDistinctRequired = len(tMap)
        formed = 0
        currentWindow = {}

        left = 0
        right = 0
        
        minimumString = ""
        minimumStringSize = float('inf')
        while right < len(s):
            if s[right] in currentWindow:
                currentWindow[s[right]] += 1
            else:
                currentWindow[s[right]] = 1
            
            if s[right] in tMap and currentWindow[s[right]] == tMap[s[right]]:
                formed += 1
            
            while formed == numberOfDistinctRequired:
                if s[left] in currentWindow and s[left] in tMap:
                    currentWindow[s[left]] -= 1
                    if currentWindow[s[left]] < tMap[s[left]]:
                        formed -= 1
                
                if right-left+1 < minimumStringSize:
                    minimumStringSize = right-left+1
                    minimumString = s[left:right+1]
                
                left += 1
            right += 1
        return minimumString
                    

                

        
        