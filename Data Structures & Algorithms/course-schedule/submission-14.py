class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        courseState = {}

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        for prerequisite in prerequisites:
            if prerequisite[0] in adjList:
                adjList[prerequisite[0]].append(prerequisite[1])
            else:
                adjList[prerequisite[0]] = [prerequisite[1]]
            
            courseState[prerequisite[0]] = UNVISITED
            courseState[prerequisite[1]] = UNVISITED
        
        def doesCourseHaveCycle(course):
            if course not in adjList:
                return False

            if adjList[course] == []:
                return False
            
            if courseState[course] == VISITING:
                return True

            if courseState[course] == VISITED:
                return False 

            courseState[course] = VISITING
            neighbours = adjList[course]

            for neighbour in neighbours:
                if doesCourseHaveCycle(neighbour):
                    return True
            
            courseState[course] = VISITED
            return False

        
        for course in adjList:
            if doesCourseHaveCycle(course):
                return False
        return True
        