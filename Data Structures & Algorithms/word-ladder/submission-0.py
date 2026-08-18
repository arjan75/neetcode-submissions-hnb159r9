from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList = {}
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                if pattern not in adjList:
                    adjList[pattern] = [word]
                else:
                    adjList[pattern].append(word)
        
        visited = set(beginWord)
        queue = deque()
        queue.append(beginWord)
        
        steps = 1
        while queue:
            for i in range(len(queue)):
                item = queue.popleft()

                if item == endWord:
                    return steps

                for j in range(len(item)):
                    pattern = item[:j] + "*" + item[j+1:]

                    for neighbour in adjList[pattern]:
                        if neighbour not in visited:
                            queue.append(neighbour)
                            visited.add(neighbour)
            
            steps += 1

        return 0  


        



        