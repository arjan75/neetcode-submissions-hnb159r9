class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        UNVISTED = 0
        VISITING = 1
        VISITED = 2

        stateMap = {}
        courseMap = {}

        for course in prerequisites:
            if course[0] in courseMap:
                courseMap[course[0]].append(course[1])
            else:
                courseMap[course[0]] = [course[1]]

            stateMap[course[0]] = 0
            stateMap[course[1]] = 0
        
        def doesCycleExist(course):
            if course not in courseMap:
                return False
            
            stateMap[course] = VISITING
            neighbours = courseMap[course]

            for neighbour in neighbours:
                if stateMap[neighbour] == VISITING:
                    return True
                    
                if doesCycleExist(neighbour):
                    return True

                
            stateMap[course] = VISITED
            return False
            
        for course in courseMap:
            if doesCycleExist(course):
                return False
        return True
        

        


            
        


        