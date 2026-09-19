class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {}
        states = {}
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        for course in prerequisites:
            if course[0] in courseMap:
                courseMap[course[0]].append(course[1])
            else:
                courseMap[course[0]] = [course[1]]
            
            states[course[0]] = UNVISITED
            states[course[1]] = UNVISITED

        def doesCycleExist(course):
            if not course in courseMap or courseMap[course] == []:
                return False
            
            if states[course] == VISITING:
                return True
            
            if states[course] == VISITED:
                return False
            
            states[course] = VISITING

            for nextCourse in courseMap[course]:
                if doesCycleExist(nextCourse):
                    return True
            
            states[course] = VISITED
            return False

        for course in courseMap:
            if doesCycleExist(course):
                return False
        return True
            

        