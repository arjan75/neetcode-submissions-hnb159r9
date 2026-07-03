class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {}
        UNVISITED = 0
        VISITING = 1
        VISITED = 2   
        stateMap = {}

        for course in prerequisites:
            if course[0] in courseMap:
                courseMap[course[0]].append(course[1])
            else:
                courseMap[course[0]] = [course[1]]  
            
            stateMap[course[0]] = UNVISITED
            stateMap[course[1]] = UNVISITED

        def doesCycleExist(course):
            if course not in courseMap:
                return False
            
            stateMap[course] = VISITING
            neighbours = courseMap[course]
            for neighbour in neighbours:
                if stateMap[neighbour] == 1:
                    return True

                if doesCycleExist(neighbour):
                    return True

            stateMap[course] = 2
            return False
        

        for course in stateMap:
            if doesCycleExist(course):
                return False
        return True




            
        


        