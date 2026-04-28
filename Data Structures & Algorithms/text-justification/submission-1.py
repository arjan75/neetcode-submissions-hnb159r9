class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        currentLine = []
        currentWidth = 0
        length = len(words)
        answer = []

        i = 0
        while i < length:
            currentWord = words[i]

            if currentWidth + len(currentWord) <= maxWidth:
                currentLine.append(currentWord)
                currentWidth += len(currentWord)+1
                i += 1
            else:
                spaces = maxWidth - currentWidth + len(currentLine)
                added = 0

                j = 0
                while added < spaces:
                    if j >= len(currentLine)-1:
                        j = 0
                    
                    currentLine[j] += " "
                    j += 1
                    added += 1
                
                answer.append("".join(currentLine))
                currentLine = []
                currentWidth = 0

        

        for i in range(len(currentLine)-1):
            currentLine[i] += " "
        
        currentLine[-1] += " " *(maxWidth-currentWidth+1)
        answer.append("".join(currentLine))
        return answer


        