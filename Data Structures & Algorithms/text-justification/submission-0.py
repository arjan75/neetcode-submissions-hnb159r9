class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        currentLine = []
        currentWidth = 0
        result = []

        i = 0
        length = len(words)
        while i < length:
            currentWord = words[i]
            if currentWidth + len(currentWord) <= maxWidth:
                # Add a new word to the line
                currentLine.append(currentWord)
                currentWidth += (len(currentWord)+1)
                i += 1
            
            else:
                # Need to adjust the spacing on next line.
                spaces = maxWidth - currentWidth + len(currentLine)
                j = 0
                added = 0

                while added < spaces:
                    if j >= len(currentLine)-1:
                        j = 0
                    
                    currentLine[j] += " "

                    j += 1
                    added += 1
                
                result.append("".join(currentLine))
                currentWidth = 0
                currentLine = []
        
        for word in range(len(currentLine)-1):
            currentLine[word] += " "
        
        currentLine[-1] += " " * (maxWidth - currentWidth+1)
        result.append("".join(currentLine))
        return result
                


        