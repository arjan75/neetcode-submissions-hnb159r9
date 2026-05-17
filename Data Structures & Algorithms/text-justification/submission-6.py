class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        currentLine = []
        width = 0
        answer = []
        i = 0
        length = len(words)
        while i < length:
            word = words[i]

            if width + len(word) <= maxWidth:
                width += (len(word)+1)
                currentLine.append(word)
                i += 1
            
            else:
                spaces = maxWidth - width + len(currentLine)
                added = 0
                j = 0
                while added < spaces:
                    if j >= len(currentLine)-1:
                        j = 0
                    currentLine[j] += " "
                    j+= 1
                    added += 1
                
                answer.append("".join(currentLine))
                currentLine = []
                width = 0
        spaces = maxWidth - width + 1

        for i in range(len(currentLine)-1):
            currentLine[i] += " "
        
        currentLine[-1] += (" "*spaces)
        answer.append("".join(currentLine))
        return answer

                


        