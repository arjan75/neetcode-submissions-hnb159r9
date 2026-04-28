class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        width = 0
        currentLine = []
        answer = []

        i = 0
        length = len(words)
        while i < length:
            currentWord = words[i]
            if width + len(currentWord) <= maxWidth:
                currentLine.append(currentWord)
                width += (len(currentWord) + 1)
                i += 1
            
            else:
                spaces = maxWidth-width+len(currentLine)
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
        
        spacesToEnd = maxWidth - width + 1
        currentLine[-1] += (" " *spacesToEnd)
        answer.append("".join(currentLine))
        return answer


        