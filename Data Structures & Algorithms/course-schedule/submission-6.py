class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True 
    
    
        preMap = {}
        stateMap = {}
        for course in prerequisites:
            if course[0] in preMap:
                preMap[course[0]].append(course[1])
            else:
                preMap[course[0]] = [course[1]]
            
            stateMap[course[0]] = 0
            stateMap[course[1]] = 0
            
            
        
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        

        def doesCourseHaveCycle(course):
            if course not in preMap:
                return False


            neighbours = preMap[course]
            stateMap[course] = VISITING
            for neighbour in neighbours:
                if neighbour in stateMap and stateMap[neighbour] == VISITING:
                    return True 
                
                if doesCourseHaveCycle(neighbour):
                    return True 
            stateMap[course] = VISITED
            return False


        for prereq in preMap:
            if doesCourseHaveCycle(prereq):
                return False
        return True

        


            
        


        