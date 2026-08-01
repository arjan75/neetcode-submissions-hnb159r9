class Solution:
    def minWindow(self, s: str, t: str) -> str:
        formed = 0
        requiredMap = {}
        for char in t:
            if char in requiredMap:
                requiredMap[char] += 1
            else:
                requiredMap[char] = 1
            
        requiredDistinct = len(requiredMap)
        formedDistinct = 0
        
        currentWindow = {}
        right = 0
        left = 0

        minlength = float('inf')
        minSubstring = ""
        while right < len(s):
            if s[right] in currentWindow:
                currentWindow[s[right]] += 1
            else:
                currentWindow[s[right]] = 1

            if s[right] in requiredMap:
                if currentWindow[s[right]] == requiredMap[s[right]]:
                    formed += 1

            while formed == requiredDistinct:
                currentWindow[s[left]] -= 1

                if s[left] in requiredMap:
                    if currentWindow[s[left]] < requiredMap[s[left]]:
                        formed -= 1
                        if currentWindow[s[left]] == 0:
                            del currentWindow[s[left]]
                if minlength > right-left+1:
                    minlength = min(minlength, right-left+1)
                    minSubstring = s[left:right+1]
                        
                left += 1
            right += 1
        return minSubstring
        
                

            


        

        