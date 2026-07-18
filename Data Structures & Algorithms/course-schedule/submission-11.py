class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        stateMap = {}

        VISITED = 2
        UNVISITED = 0
        VISITING = 1

        for course in prerequisites:
            if course[0] in adjList:
                adjList[course[0]].append(course[1])
            else:
                adjList[course[0]] = [course[1]]
            
            stateMap[course[0]] = UNVISITED
            stateMap[course[1]] = UNVISITED
        
    
        def doesCycleExist(course):
            if course not in adjList:
                return False
            
            if stateMap[course] == VISITING:
                return True
            
            stateMap[course] = VISITING

            neighbours = adjList[course]
            for neighbour in neighbours:
                if doesCycleExist(neighbour):
                    return True

            stateMap[course] = VISITED
            return False


        for course in adjList:
            if doesCycleExist(course):
                return False
        return True

        

        