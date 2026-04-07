class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getKey(str1):
            lst = [0]*26
            for s in str1:
                index = ord(s)-97
                lst[index] += 1
            key = ""
            for i in range(26):
                if lst[i] != 0:
                    key += (lst[i]*chr(i+97))
            return key
        
        anagramsMap = {}
        for s in strs:
            key = getKey(s)
            if key in anagramsMap:
                anagramsMap[key].append(s)
            else:
                anagramsMap[key] = [s]
            
        output = []
        for key in anagramsMap:
            output.append(anagramsMap[key])
        return output

            

            

        