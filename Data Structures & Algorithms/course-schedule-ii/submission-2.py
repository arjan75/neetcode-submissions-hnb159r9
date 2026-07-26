class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        output = []
        adjList = {}
        stateMap = {}
        
        for prereq in prerequisites:
            if prereq[0] in adjList:
                adjList[prereq[0]].append(prereq[1])
            else:
                adjList[prereq[0]] = [prereq[1]]
        
        for i in range(numCourses):
            stateMap[i] = UNVISITED
            if i not in adjList:
                adjList[i] = []
        
        def doesCycleExist(course):
            if stateMap[course] == VISITED:
                return False
            
            if stateMap[course] == VISITING:
                return True
            
            stateMap[course] = VISITING
            
            for neighbour in adjList[course]:
                if doesCycleExist(neighbour):
                    return True
            
            stateMap[course] = VISITED
            output.append(course)
            return False
        
        for i in range(numCourses):
            if doesCycleExist(i):
                return []
        return output 


        

        