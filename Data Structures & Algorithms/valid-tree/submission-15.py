class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = {}
        if not edges:
            return True

        for edge in edges:
            if edge[0] in edgeMap:
                edgeMap[edge[0]].append(edge[1])
            else:
                edgeMap[edge[0]] = [edge[1]]

            if edge[1] in edgeMap:
                edgeMap[edge[1]].append(edge[0])
            else:
                edgeMap[edge[1]] = [edge[0]]

        
        visited = set()

        def isTree(current, previous):
            if current in visited:
                return False
            
            neighbours = edgeMap[current]
            visited.add(current)

            for neighbour in neighbours:
                if neighbour == previous:
                    continue
                
                if neighbour in visited:
                    return False
                
                if not isTree(neighbour, current):
                    return False
                
            return True
        
        if isTree(0, -1) and len(visited) == n:
            return True
        
        return False
        


        

        