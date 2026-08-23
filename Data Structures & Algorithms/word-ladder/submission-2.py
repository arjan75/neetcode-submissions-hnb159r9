from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)

        patterns = {}
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]

                if pattern in patterns:
                    patterns[pattern].append(word)
                else:
                    patterns[pattern] = [word]
        
        queue = deque([beginWord])


        steps = 1
        visited = set()
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return steps

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    neighbours = patterns[pattern]

                    for neighbour in neighbours:
                        if neighbour not in visited:
                            queue.append(neighbour)
                            visited.add(neighbour)

            steps += 1
        return 0 





        
        