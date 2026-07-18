class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for course in prerequisites:
            if course[0] in adjList:
                adjList[course[0]].append(course[1])
            else:
                adjList[course[0]] = [course[1]]
        
        visited = set()
        def doesCycleExist(course):
            if course not in adjList:
                return False
            
            if course in visited:
                return True
            
            visited.add(course)

            neighbours = adjList[course]
            for neighbour in neighbours:
                if doesCycleExist(neighbour):
                    return True

            visited.remove(course)
            return False


        for course in adjList:
            if doesCycleExist(course):
                return False
        return True

        

        