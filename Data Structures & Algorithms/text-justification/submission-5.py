class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        currentLine = []
        width = 0
        i = 0
        length = len(words)
        answer = []

        while i < length:
            word = words[i]
            if width + len(word) <= maxWidth:
                currentLine.append(word)
                width += (len(word) +1)
                i += 1
            
            else:
                spaces = maxWidth - width + len(currentLine)
                added = 0 
                j = 0

                while added < spaces:
                    if j >= len(currentLine)-1:
                        j = 0
                    
                    currentLine[j] += " "
                    j += 1
                    added += 1
                
                answer.append("".join(currentLine))
                width = 0
                currentLine = []
        
        for i in range(len(currentLine)-1):
            currentLine[i] += " "
        
        spaces = maxWidth-width+1
        currentLine[-1] += (" "*spaces)
        answer.append("".join(currentLine))
        return answer


        