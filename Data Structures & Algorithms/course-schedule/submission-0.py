class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for course in prerequisites:
            if course[0] in adjList:
                adjList[course[0]].append(course[1])
            else:
                adjList[course[0]] = [course[1]]


        visited = set()

        def canTakeCourse(course):
            if course in visited:
                return False
            
            if course not in adjList:
                return True
                
            if adjList[course] == []:
                return True
            
            visited.add(course)
            for prereq in adjList[course]:
                if not canTakeCourse(prereq):
                    return False
            
            visited.remove(course)
            adjList[course] = []
            return True
        

        for course in adjList:
            if not canTakeCourse(course):
                return False
        return True