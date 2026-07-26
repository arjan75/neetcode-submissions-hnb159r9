class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}
        stateMap = {}
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        for prereq in prerequisites:
            if prereq[0] in adjList:
                adjList[prereq[0]].append(prereq[1])
            else:
                adjList[prereq[0]] = [prereq[1]]
            

            stateMap[prereq[0]] = UNVISITED
            stateMap[prereq[1]] = UNVISITED

        for i in range(numCourses):
            if i not in adjList:
                adjList[i] = []
            
            if i not in stateMap:
                stateMap[i] = UNVISITED
            
        
        output = []

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

        


        