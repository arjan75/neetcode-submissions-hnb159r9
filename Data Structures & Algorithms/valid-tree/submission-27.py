class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}
        if not edges:
            return True
            
        for edge in edges:
            if edge[0] in adjList:
                adjList[edge[0]].append(edge[1])
            else:
                adjList[edge[0]] = [edge[1]]
            
            if edge[1] in adjList:
                adjList[edge[1]].append(edge[0])
            else:
                adjList[edge[1]] = [edge[0]]
        
        visited = set()
        def doesCycleExist(current, parent):
            if current in visited:
                return True
            
            if current not in adjList:
                return False

            neighbours = adjList[current]
            visited.add(current)
            for neighbour in neighbours:
                if neighbour == parent:
                    continue
                
                if doesCycleExist(neighbour, current):
                    return True
            return False
            

        if doesCycleExist(0, -1) or len(visited) != n:
            return False
        return True
        

            


        