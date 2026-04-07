class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charSeen = {}
        for i in s:
            if i in charSeen:
                charSeen[i] += 1
            else:
                charSeen[i] = 1
        
        charSeen2 = {}
        for i in t:
            if i in charSeen2:
                charSeen2[i] += 1
            else:
                charSeen2[i] = 1
        
        for key in charSeen2:
            if key not in charSeen or charSeen[key] != charSeen2[key]:
                return False
        
        for key in charSeen:
            if key not in charSeen2 or charSeen[key] != charSeen2[key]:
                return False
        return True

        