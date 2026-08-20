from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        wordSet.add(beginWord)
        adjList = {}
        for word in wordSet:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                if pattern in adjList:
                    adjList[pattern].append(word)
                else:
                    adjList[pattern] = [word]
        
        queue = deque()
        queue.append(beginWord)
        visited = set()
        visited.add(beginWord)

        steps = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return steps 

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]

                    neighbours = adjList[pattern]

                    for neighbour in neighbours:
                        if neighbour not in visited:
                            queue.append(neighbour)
                            visited.add(neighbour)
            steps += 1
        return 0
                    

        