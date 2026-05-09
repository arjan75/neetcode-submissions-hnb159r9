class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        currentLine = []
        answer = []
        width = 0
        i = 0
        while i < len(words):
            word = words[i]
            if len(word) + width <= maxWidth:
                width += (len(word)+1)
                currentLine.append(word)
                i += 1
            else:
                ## you cannot fit in the current line
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
        spacesToEnd = maxWidth-width+1
        currentLine[-1] += (" "* spacesToEnd)
        answer.append("".join(currentLine))
        return answer



        