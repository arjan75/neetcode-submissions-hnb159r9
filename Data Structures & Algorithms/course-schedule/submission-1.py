class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqs = {}
        for course in prerequisites:
            if course[0] in  preReqs:
                preReqs[course[0]].append(course[1])
            else:
                preReqs[course[0]] = [course[1]]
        
        visited = set()
        def findCycle(course):
            if course in visited:
                return True
            
            if course not in preReqs:
                return False
            
            if preReqs[course] == []:
                return False
            
            visited.add(course)
            for preReqCourse in preReqs[course]:
                if findCycle(preReqCourse):
                    return True

            visited.remove(course)
            return False

        for course in preReqs:
            if findCycle(course):
                return False
        
        return True


        