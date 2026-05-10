class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        width = 0
        currentLine = []
        i = 0
        length = len(words)
        answer = []

        while i < length:
            currentWord = words[i]
            if width + len(currentWord) <= maxWidth:
                currentLine.append(currentWord)
                width += (len(currentWord)+1)
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
        
        spaces = maxWidth - width + 1
        for i in range(len(currentLine)-1):
            currentLine[i] += " "
        
        currentLine[-1] += (" " * spaces)
        answer.append("".join(currentLine))
        return answer



        

        